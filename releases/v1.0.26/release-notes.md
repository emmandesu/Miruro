## PiP fixes
- Removes the duplicate native audio-focus controller that could repeatedly pause WebView playback.
- Moves the PiP button into the native player overlay on the left, with the existing control visibility and touch-lock behavior.
- Avoids stopping a PiP window that remains visibly active during device lifecycle callbacks.
- Keeps explicit Play/Pause actions and the existing video/iframe.

Install over the current app. The signed API 36 build and automated checks pass; the reported Xiaomi playback behavior still needs confirmation on the phone.
