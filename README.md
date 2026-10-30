# Miruro

Independent Android client by Emmanuel Flores. Not affiliated with Miruro or AniList.

## Download

Get the latest signed APK from [GitHub Releases](https://github.com/emmandesu/Miruro/releases). Miruro 1.0.15 and newer connect to this repository; older builds need a one-time manual update.

After that, use **Client Settings → Support → App updates**. The app checks once daily when opened, or when you tap Check for updates. It downloads the APK inside the app, verifies its checksum, package, version and installed signing identity, then asks Android to show its installation prompt. Update notices show What's new, with fixes and new features. Installed-release notes are also available after a successful check. Update notices wait while you are watching. A finish-watching option queues a reminder after leaving the watch page.

The app contains no GitHub token. It uses the selected DNS provider for checks and downloads. Android may ask you to allow installs from Miruro before the first in-app installation.

The screen stays awake while a trusted Miruro video plays inline or in fullscreen, and normal sleep is allowed when paused, ended or backgrounded. Client Settings dialog headers use the Miruro logo.

**Client Settings → Support → Licenses & credits** lists the bundled AndroidX libraries, Chromium boundary interfaces and Karla font. Full Apache 2.0, BSD 3-Clause and OFL 1.1 texts are included for offline reading, alongside project links and acknowledgements. About Miruro links to the same page.

## Episode downloads

Open **Downloads** in Miruro’s main menu to see active progress, the waiting queue and completed videos. Add up to 20 pending episodes; they download one at a time using the DNS provider selected when each starts. Tap **×** to cancel one active or queued item. Tap a completed video for Android’s **Open with** chooser and select a video player.

Finished history is kept locally, with up to 100 items. Clearing it keeps the saved files. If Android stops the app, prepare new links for interrupted jobs; partial transfers do not resume. Files saved with older app versions remain in their folders but cannot automatically appear in the new history.

## Bell and Android notifications

Miruro and AniList unread counts are mirrored as Android notifications, with episode details added when the site’s Notifications panel renders them. Tapping a site alert opens the bell. App updates appear inside that panel too, with a separate unread dot and a link to release notes and update controls. Compatible app releases can also create an Android alert once per version.

Use **Client Settings → Support → Notification settings** to choose site and app-update alerts, allow Android notification permission, or change Android categories and sound. Site alerts sync as the page receives them and on reopening. This does not provide server push while Android has closed the app; update checks remain daily on opening or manual. No web-session credentials are copied into a background service.

## Recovery and notification fixes in 1.0.20

Renderer recovery now disposes of the failed WebView and stops its polling before reopening. DNS changes follow the current page, and activity restoration retains safe episode selectors. Signing out clears old account notices. Newly observed notice IDs can alert even when the unread count is unchanged; older/filter-loaded rows remain quiet. Opening app updates from any entry point clears the bell’s unread indicator and available-update alert.

The release passes 860 automated checks and retains the owner signing identity. Native renderer-recovery and signed-in Android notification delivery still need a phone check.

## Fullscreen rotation in 1.0.21

A rotation button above the touch lock lets you lock or unlock fullscreen orientation. Fullscreen starts locked in landscape. Tap to auto rotate, turn the phone, then tap again to hold the current angle. Exiting fullscreen restores the app's previous rotation setting.

The phone-and-lock and rotating-phone icons match the touch lock's white line style, translucent round surface and 48 dp tap target. They fade with the player controls. While touch lock is enabled, only Unlock is available; unlock touches first to change rotation. A short guide is included in Client Settings → General → Player.

The release passes 898 automated checks, including fullscreen lifecycle, saved rotation preferences and touch-lock interaction. The APK is signed with the original owner identity. Physical rotation, cutout placement and provider fullscreen behavior still need a device check.

## Current-stream downloads in 1.0.22

The player's existing Download icon now captures the selected supported stream, checks its layout, and asks where to save the full episode. It joins the same queue with progress, cancellation and completed-file opening. Adding from fullscreen keeps fullscreen when you return from the save picker.

The current integration covers the observed pinewren.top CDN used by the sun player. It reads the actual selected HLS source rather than its temporary MSE blob. Playlists and video chunks use the DNS provider selected when the job starts. Requests stay on approved routes at the same source host; unrelated redirects and external windows are blocked. Every media chunk is checked as binary video, even when named as an image.

Complete plain HLS with embedded audio saves as **.ts**, for compatible players such as VLC. Supported direct/fragmented MP4 stays **.mp4**. Separate player captions are not included; HLS progress and size are estimates. Encrypted, live and unsupported layouts show a message. The episode menu → Download still offers the existing provider MP4 route. Stream URLs can expire while queued; interrupted jobs need a fresh link.

The release passes **990 automated checks**. A short live two-chunk sample processed by the transfer code was identified as 1080p H.264 with AAC audio. Full Android tap/picker/queue behavior and live native custom-DNS transfers still need a phone check; this environment could not complete a native outbound DoH tunnel.

## Publishing later versions

This repository stores public, pre-signed release files. Upload the four prepared files to `releases/vVERSION/` in one commit: the APK, `update.json`, `SHA256SUMS.txt` and `release-notes.md`.

The publisher verifies the owner signing certificate and checksums, creates the versioned GitHub Release, downloads its public assets to verify them, and only then advances the root `update.json` used by installed apps. It refuses to replace a published version with different files or roll metadata backwards. Publishing uses GitHub's temporary token scoped to this repository; no personal token or signing key is stored here.

Use the original owner key and a higher numeric versionCode for each new release. Signing happens privately before upload. Do not upload private source archives, keystores, key passwords or other credentials.

## Verification limits

The Android APK is build- and signature-verified. Automated checks cover update addresses, package/version/signing identity, checksums, transfer failures and cancellation. Queue order, per-item cancellation, interrupted-state recovery and menu integration are also covered by automated checks. Android permission prompts, video-player chooser behavior, background transfers and installation still need physical device verification.



