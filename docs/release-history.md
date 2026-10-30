# Release history

For complete notes and APK assets, see [GitHub Releases](https://github.com/emmandesu/Miruro/releases).

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

## Community sign-in in 1.0.23

The comments panel uses The Anime Community, separately from AniList. The client now allows that service's exact HTTPS host in both the early popup guard and native document policy, including the embedded widget's blank-window bootstrap. Login and registration retain their original WebView, shared cookie profile and opener connection.

Simultaneous pending windows have separate guards and timeouts, so a hidden ad candidate no longer consumes the login or download window. Unrelated external destinations and lookalike origins remain blocked. Authentication opened in the main view does not restart the anime loading screen.

The release passes **1,087 automated checks** and retains the original owner signing identity. The provider was unavailable from the build environment; live account login, registration, commenting and Android session persistence still need device verification. Provider-specific social sign-in was not inspected or verified.

## Android 16 / API 36 in 1.0.24

Miruro now compiles against and targets **API 36**, while retaining **Android 9+** support (minimum API 28). The Android Studio project uses AGP 8.10.1, Gradle 8.11.1 and Build Tools 36.0.0. The direct SDK build reads its SDK levels and version from the same Gradle configuration, and release preparation verifies those settings against the compiled APK.

The existing edge-to-edge layout and modern Back callback remain active. MainActivity explicitly enables the platform Back callback and uses Android 16's temporary large-screen compatibility setting to preserve the fullscreen landscape/orientation-lock feature. The app does not opt out of edge-to-edge, set a fixed aspect ratio or disable normal window resizing. This compatibility setting is specific to the API 36 migration and will need review before targeting later Android versions.

The release retains community login-window support, download queues, selected-DNS transfers and the existing update flow. All **1,087 automated regression checks** pass. The signed APK's compiled/target SDK 36, minimum SDK 28, versionCode 25 and original owner certificate are verified. Release preparation also rejects the previous API 35 APK. Physical Android 16 gestures, keyboard, fullscreen and tablet/foldable rotation still need device verification; live community account sign-in remains unverified here.

## Picture in picture in 1.0.25

The player has a round PiP button at the top-left of its controls. Client Settings → General → Player → Picture in picture provides manual entry, automatic-entry preference and an Android permission shortcut. Automatic entry when leaving a currently playing supported video is enabled by default; paused, ended and stale playback cannot arm it. Dialogs, login windows and native save flows block entry.

PiP keeps the current Activity, WebView, video and iframe. Scoped layout markers fill the small window with the existing stream and hide surrounding UI; expanding removes those markers and restores the page. Android supplies Play/Pause, expand and close controls. Closing pauses playback. Support covers the exact HTTPS strm.cx player and direct Miruro media-player/control-enabled video. The Android platform feature, permission and an updated WebView are required.

A non-exported media-playback foreground service displays a low-priority return-to-player notification while PiP is active. It allows new audio-focus requests under Android 15+ rules and ends when PiP closes, expands, fails, or its activity is disposed. Audio-focus loss pauses the stream. No second media URL/player is created, and DNS, popup filtering and download behavior stay on the existing paths.

The signed API 36 release is versionCode 26 and passes **1,185 automated checks**, including 60 PiP origin/state checks and 38 existing-player/layout/command checks. Physical Android PiP transitions, OEM permission screens, native/iframe rendering, audio focus and RemoteAction delivery still need device verification. No live Android PiP success is claimed from this build environment.
