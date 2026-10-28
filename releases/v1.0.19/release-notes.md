## New features
- Mirror Miruro and AniList unread notices as Android notifications.
- Tap a site alert to return to Miruro’s bell panel.
- App updates now appear inside the Notifications panel, with release-note and update controls.
- A separate dot on the bell marks an unread app update.
- Available app releases also get an Android notification once per version.
- Add Notification settings under Client Settings → Support, with separate site/update alert switches.

## Improvements
- Group old unread notices instead of flooding the notification tray.
- Reading notices updates or clears the Android summary without repeated sounds.
- Keep the website’s own notification count and Miruro/AniList controls intact.
- Handle Android notification permission and category settings gracefully.
- Restrict the notification bridge to the trusted top-level Miruro page.

## Delivery notes
- Site alerts sync as the website receives them and when the app reopens. Details appear when the site panel renders them.
- This is not server push while Android has closed the app. Update checks remain daily on opening or manual.
- Install over your current Miruro app to retain settings and sign-in.
