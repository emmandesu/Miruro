## Fixes
- Allows the comments panel's Log In and Sign Up windows for The Anime Community.
- Preserves the original login window and its connection to the embedded comments, including blank-window sign-in bootstraps.
- Separates simultaneous pending windows so a hidden ad attempt does not occupy the real login or download window.
- Keeps unrelated popup destinations and redirects blocked. Community access is restricted to its exact HTTPS host.

## Notes
- Community accounts are separate from AniList sign-in. Use the community panel's Log In or Sign Up buttons.
- Login uses the website's own forms and shared WebView cookies; the app does not copy credentials or log authentication URLs.
- 1,087 automated checks pass and the APK retains the original signing identity. A real Android account login, registration and commenting still need device verification: the community service could not be accessed from the build environment.
- Install over the existing app to retain settings, downloads and sign-in.
