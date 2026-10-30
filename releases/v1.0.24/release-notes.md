## Android 16 update
- Miruro now compiles against and targets API 36 (Android 16).
- Android 9 and newer remain supported; minimum API stays at 28.
- Keeps immersive fullscreen, touch/orientation locks and the existing modern Back handler.
- Preserves fullscreen rotation locking on Android 16 large screens through the platform compatibility option.

## Build improvements
- Updated Android build tooling and aligned the Android Studio and direct SDK build settings.
- Retains the community login-window fix, download queue and selected-DNS transfers.

## Notes
- Install over your current app to retain settings, downloads and sign-in.
- Signed build, SDK metadata and automated regressions are checked. Android 16 gestures, keyboard, fullscreen and tablet/foldable behavior still need physical-device verification. Live community account sign-in remains unverified in this environment.
