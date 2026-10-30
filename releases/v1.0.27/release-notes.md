## Detailed diagnostics
- Adds player Play/Pause, buffering, stalled/no-progress, seek, decode/error and visibility events with position, buffer and player state.
- Correlates app-issued PiP commands with command-received and video events, including caught Play permission/autoplay failures.
- Logs PiP entry decisions, permissions, state blockers, lifecycle, service events, renderer stalls, memory pressure and categorized script/resource failures.
- Adds a live event viewer with pauseable refresh, a state-snapshot/issue marker and structured JSON export with a field guide.
- Export includes app/WebView/device context and recent Android process-exit codes where available.

## Privacy and limits
- Recording stays opt-in and local. Full URLs, credentials, response/page text and raw console/exception messages are excluded.
- Logs rotate within 1 MB. Event-rate suppression is reported; resource timing/status availability depends on WebView.
- A pause without a recent app command is recorded as an observation, not proof of its cause. Logging cannot capture events that happened before recording was enabled.

## Verification
- 1,210 automated checks pass. API 36, Android 9+ support and the original signer are retained. Actual Android event delivery and physical-device PiP behavior still need device verification.
