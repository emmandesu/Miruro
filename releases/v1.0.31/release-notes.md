# Miruro 1.0.31

## Fixes
- Fixed brightness controls staying missing after player resets or episode changes in fullscreen. Exiting and re-entering fullscreen is no longer needed for this recovery path.
- Restored the slider correctly after temporary view reattachment, resize, background/resume and window visibility changes.
- Preserved normal control fading, touch lock, PiP/settings suspension and system-brightness restoration.

## Diagnostics
- Added native player-overlay and brightness state to opt-in logs and exported snapshots to help diagnose visibility issues.

Signed with the original Miruro certificate. Regression tests reproduce the old reset failure and pass with this repair; confirmation on the affected phone is still needed.
