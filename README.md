# Miruro

Independent Android client by Emmanuel Flores. Not affiliated with Miruro or AniList.

## Download

Get the latest signed APK from [GitHub Releases](https://github.com/emmandesu/Miruro/releases). Miruro 1.0.15 and newer connect to this repository; older builds need a one-time manual update.

After that, use **Client Settings → Support → App updates**. The app checks once daily when opened, or when you tap Check for updates. It downloads the APK inside the app, verifies its checksum, package, version and installed signing identity, then asks Android to show its installation prompt. Update notices show What's new, with fixes and new features. Installed-release notes are also available after a successful check. Update notices wait while you are watching. A finish-watching option queues a reminder after leaving the watch page.

The app contains no GitHub token. It uses the selected DNS provider for checks and downloads. Android may ask you to allow installs from Miruro before the first in-app installation.

The screen stays awake while a trusted Miruro video plays inline or in fullscreen, and normal sleep is allowed when paused, ended or backgrounded. Client Settings dialog headers use the Miruro logo.

## Publishing later versions

This repository stores public, pre-signed release files. Upload the four prepared files to `releases/vVERSION/` in one commit: the APK, `update.json`, `SHA256SUMS.txt` and `release-notes.md`.

The publisher verifies the owner signing certificate and checksums, creates the versioned GitHub Release, downloads its public assets to verify them, and only then advances the root `update.json` used by installed apps. It refuses to replace a published version with different files or roll metadata backwards. Publishing uses GitHub's temporary token scoped to this repository; no personal token or signing key is stored here.

Use the original owner key and a higher numeric versionCode for each new release. Signing happens privately before upload. Do not upload private source archives, keystores, key passwords or other credentials.

## Verification limits

The Android APK is build- and signature-verified. Automated checks cover update addresses, package/version/signing identity, checksums, transfer failures and cancellation. Android permission prompts and installation behavior still need physical device verification.
