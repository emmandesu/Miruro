# Miruro 1.0.29

## Security
- Protected the app's local DNS proxy with fresh session credentials, bounded authentication and fixed header deadlines.
- Browsing, download and update connections keep using the selected DNS provider. Proxy authentication is prepared before the website loads; there is no silent DNS fallback.

## Fixes
- Client dialogs and live diagnostic refresh now stop cleanly when the app screen is destroyed or replaced. Log reading runs off the UI thread.
- Download pages and popup probes now dispose of failed web renderers safely.
- Download file permissions are tracked across restarts and released when no longer needed. Completed videos are kept.

Signed with the original Miruro certificate. Android WebView authentication and heap behavior still need device confirmation.
