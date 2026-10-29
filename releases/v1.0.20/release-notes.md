## Fixes
- Safely detach and destroy a crashed WebView before offering to reopen it; stop player polling and stale callbacks.
- Keep the current page when changing DNS after navigating inside Miruro.
- Restore the selected episode after activity recreation, retaining safe episode selectors without saving login tokens.
- Clear old Android notices on sign-out and reset notification history for the next account.
- Recognize a newly observed episode or AniList notice even when the unread count stays the same.
- Clear the app-update unread dot and available-update alert when opening updates from Client Settings or any other entry point.

## Improvements
- Keep old notices, source-tab changes and manual filter/load-more actions quiet.
- Preserve notification deduplication across restarts with bounded digest history.
- Reopening after an initial-load renderer failure still waits for startup; successful startup does not repeat the splash.

## Notes
- Site notifications still depend on the website receiving/rendering them; this is not server push while Android has closed the app.
- Install over your current Miruro app to retain settings and sign-in.
