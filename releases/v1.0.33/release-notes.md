# Miruro 1.0.33

## Player
- Removed the wide dark bar behind the episode title. Small white text with a soft shadow sits directly over the video.
- Fixed the inline title being pushed down by a notch offset that was already above the player.
- Reserved space between the title and brightness slider to prevent overlap on smaller players.
- Preserved fullscreen cutout protection, title shortening and control fading through resizing and fullscreen return.

## Diagnostics
- Added numeric title/slider positions and effective safe insets to opt-in overlay logs. Episode text is not recorded.

Signed with the original Miruro certificate. The previous inset failure was reproduced and the corrected regression checks pass. Visual confirmation on the phone is still needed. The TV edition is unchanged.
