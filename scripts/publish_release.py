#!/usr/bin/env python3
"""Publish pre-signed APKs, then advance update.json. Never builds or signs apps.
Runs on GitHub Actions with its repository-scoped GITHUB_TOKEN via gh.
"""
from pathlib import Path
import base64
import hashlib
import json
import os
import re
import subprocess
import tempfile

REPO = 'emmandesu/Miruro'
CERT = 'ae56813d94cc74bd7b79262808085979af1d721235db0ec8e52a4a675730799f'


def gh(*args, required=True):
    result = subprocess.run(['gh', *map(str, args)], text=True, capture_output=True)
    if required and result.returncode:
        raise RuntimeError(result.stderr.strip() or 'GitHub operation failed')
    return result


def optional_api(endpoint):
    result = gh('api', endpoint, required=False)
    if result.returncode == 0:
        return json.loads(result.stdout)
    if '(HTTP 404)' in result.stderr:
        return None
    raise RuntimeError(result.stderr.strip() or 'GitHub API unavailable')


def validate(folder):
    meta = json.loads((folder / 'update.json').read_text())
    version = meta.get('versionName', '')
    if not re.fullmatch(r'[0-9]{1,5}\.[0-9]{1,5}\.[0-9]{1,5}', version):
        raise ValueError('Invalid release version')
    filename = f'Miruro-{version}.apk'
    if folder.name != f'v{version}' or meta.get('schema') != 1 or meta.get('packageName') != 'com.emflo.miruro':
        raise ValueError('Unexpected release identity')
    if type(meta.get('versionCode')) is not int or not 1 <= meta['versionCode'] <= 2147483647:
        raise ValueError('Invalid version code')
    if type(meta.get('minSdk')) is not int or not 28 <= meta['minSdk'] <= 100:
        raise ValueError('Invalid minimum SDK')
    if meta.get('apkUrl') != f'https://github.com/{REPO}/releases/download/v{version}/{filename}':
        raise ValueError('Unapproved APK URL')
    apk = folder / filename
    digest = hashlib.sha256(apk.read_bytes()).hexdigest()
    if not 0 < apk.stat().st_size <= 128 * 1024 * 1024 or meta.get('size') != apk.stat().st_size or meta.get('sha256') != digest:
        raise ValueError('APK size/checksum mismatch')
    if (folder / 'SHA256SUMS.txt').read_text() != f'{digest}  {filename}\n':
        raise ValueError('Checksum file mismatch')
    notes = (folder / 'release-notes.md').read_text().strip()
    if meta.get('notes') != notes or len(notes) > 8000 or '\0' in notes:
        raise ValueError('Release notes mismatch')
    allowed = {filename, 'update.json', 'SHA256SUMS.txt', 'release-notes.md'}
    if {p.name for p in folder.iterdir()} != allowed or any(p.is_symlink() for p in folder.iterdir()):
        raise ValueError('Only public release files may be published')
    return meta, apk


def verify_signature(apk):
    sdk = os.environ.get('ANDROID_HOME') or os.environ.get('ANDROID_SDK_ROOT')
    jars = sorted(Path(sdk).glob('build-tools/*/lib/apksigner.jar')) if sdk else []
    if not jars:
        raise RuntimeError('Android SDK apksigner is required to verify the owner certificate')
    result = subprocess.run(['java', '-jar', str(jars[-1]), 'verify', '--print-certs', str(apk)], text=True, capture_output=True, check=True)
    if f'Signer #1 certificate SHA-256 digest: {CERT}' not in result.stdout:
        raise ValueError('APK has the wrong signing certificate')


def publish(root):
    if os.environ.get('GITHUB_REPOSITORY') != REPO or os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise RuntimeError('Publishing is restricted to the owner repository main branch')
    candidates = [validate(p.parent) for p in (root / 'releases').glob('*/update.json')]
    if not candidates:
        raise RuntimeError('No release files staged')
    meta, apk = max(candidates, key=lambda pair: pair[0]['versionCode'])
    verify_signature(apk)
    folder = apk.parent
    version = meta['versionName']
    tag = f'v{version}'
    pointer = optional_api(f'repos/{REPO}/contents/update.json?ref=main')
    if pointer:
        previous = json.loads(base64.b64decode(pointer['content']))
        if previous['versionCode'] > meta['versionCode']:
            raise RuntimeError('Refusing to roll update metadata backwards')
        if previous['versionCode'] == meta['versionCode'] and previous != meta:
            raise RuntimeError('Published versions are immutable; bump the version')
    existing = optional_api(f'repos/{REPO}/releases/tags/{tag}')
    assets = [apk, folder / 'SHA256SUMS.txt', folder / 'update.json']
    if existing is None:
        target = os.environ.get('GITHUB_SHA', '')
        if not re.fullmatch(r'[0-9a-f]{40}', target):
            raise ValueError('Missing commit SHA')
        gh('release', 'create', tag, *assets, '--repo', REPO, '--target', target,
           '--title', f'Miruro {version}', '--notes-file', folder / 'release-notes.md')
    elif existing.get('draft') or existing.get('prerelease'):
        raise RuntimeError('Existing version is not a stable published release')
    # Verify the actual public assets before pointing installed apps to them.
    with tempfile.TemporaryDirectory() as temp:
        for asset in assets:
            gh('release', 'download', tag, '--repo', REPO, '--pattern', asset.name, '--dir', temp)
            downloaded = Path(temp) / asset.name
            if hashlib.sha256(downloaded.read_bytes()).digest() != hashlib.sha256(asset.read_bytes()).digest():
                raise ValueError('Published release asset differs from the staged file')
    if pointer is None or json.loads(base64.b64decode(pointer['content'])) != meta:
        request = {'message': f'Activate Miruro {version} in-app updates',
                   'content': base64.b64encode((folder / 'update.json').read_bytes()).decode(), 'branch': 'main'}
        if pointer:
            request['sha'] = pointer['sha']
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'request.json'
            path.write_text(json.dumps(request))
            gh('api', '--method', 'PUT', f'repos/{REPO}/contents/update.json', '--input', path)
    # Read the live API pointer back after mutation, to detect incomplete publication.
    live = optional_api(f'repos/{REPO}/contents/update.json?ref=main')
    if not live or json.loads(base64.b64decode(live['content'])) != meta:
        raise RuntimeError('Live update metadata verification failed')
    print(f'Published Miruro {version}: signed APK and live update metadata verified.')


if __name__ == '__main__':
    publish(Path.cwd())
