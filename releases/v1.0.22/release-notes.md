## New feature
- The player Download icon now captures the current supported stream and adds the full episode to Downloads, without opening an external download page.
- Uses your selected DNS provider for playlists and video chunks, with progress, cancellation and completed-file opening.

## Improvements
- Captures the actual selected HLS source instead of the temporary playback blob.
- Verifies video chunks even when the provider gives them image filenames.
- Blocks unapproved redirects and prevents duplicate downloads from one tap.
- Keeps fullscreen after adding a stream download; cancelling a fullscreen panel restores the lock buttons.

## Notes
- Supported HLS video saves as .ts; use a compatible player such as VLC. Supported MP4 sources remain .mp4. Separate captions are not included.
- Current direct-stream support covers the observed pinewren.top CDN used by the sun player. Unsupported/encrypted layouts show a message; use the episode menu → Download for the provider MP4 route.
- Stream links may expire in the queue. Interrupted downloads require a fresh link.
- Install over the current app to keep settings and sign-in. The Android save flow and live custom-DNS transfer still need a phone check.
