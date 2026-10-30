## Picture in picture
- Watch the current streaming video in a small Android window while using other apps.
- Tap the new Picture in picture button at the player’s top-left, or use Client Settings → General → Player → Picture in picture.
- Automatic entry when leaving during playback is enabled by default and can be turned off in those settings. Paused videos and pages without active supported playback do not enter automatically.
- Android’s small window provides Play/Pause, expand and close controls. Expanding returns to the existing player; closing pauses playback.

## Playback handling
- Keeps the existing video and iframe without loading a second stream.
- Hides the surrounding site, player controls and client overlays while PiP is active, then restores their layout.
- Adds a playback notification/service for Android 16 audio-focus handling. It ends when PiP closes, expands, or fails to open.
- Supports the current strm.cx player and direct Miruro media-player/control-enabled video. Android PiP support and permission are required.

## Notes
- API 36 target and Android 9+ support are retained. Install over the current app to keep data.
- 1,185 automated checks pass. The APK builds with the original signing certificate. Actual Android PiP transitions, OEM permission screens, media-control delivery and audio focus still need physical-device verification.
