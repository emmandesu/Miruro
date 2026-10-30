# Publishing Miruro releases

## Release process

This repository stores public, pre-signed release files. Upload the four prepared files to `releases/vVERSION/` in one commit: the APK, `update.json`, `SHA256SUMS.txt` and `release-notes.md`.

The publisher verifies the owner signing certificate and checksums, creates the versioned GitHub Release, downloads its public assets to verify them, and only then advances the root `update.json` used by installed apps. It refuses to replace a published version with different files or roll metadata backwards. Publishing uses GitHub's temporary token scoped to this repository; no personal token or signing key is stored here.

Use the original owner key and a higher numeric versionCode for each new release. Signing happens privately before upload. Do not upload private source archives, keystores, key passwords or other credentials.

