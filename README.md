# jukebox
Simple Python script for playing sound files. By default plays a random selection from a pre-set directory.

@author: codequiver (github.com/codequiver)

GitHub Source: [https://github.com/CodeQuiver/jukebox](https://github.com/CodeQuiver/jukebox)

This script will play a random mp3 or wav sound file from a set folder when activated. 
By default, the directory/folder is "./jukebox_sound".

Alternatively, a specific sound file name or a specific folder can be passed as argument(s).

The script can be called with `--set-default-sound-folder` to change the source folder going forward.
This setting will be stored in `default_sound_folder.config`. (The `--folder` flag does *not* include this functionality.)

Args:
--sound                        Name of a specific sound file to play.
--folder                       Path to a specific folder to search for sound files, instead of the stored setting.
--set-default-sound-folder     Set a folder as the new default folder to search for sound files. Relative or absolute path both work.
--get-default-sound-folder     Print the current default sound folder stored in `default_sound_folder.config`, then exit script.

Sample Usage:
    python jukebox.py                                                           --> randomly plays an mp3 or wav file from the default folder
    python jukebox.py --sound "metal_dragon_battle.mp3"                         --> plays "metal_dragon_battle.mp3"
    python jukebox.py --folder "./bard_songs"                                   --> randomly plays an mp3 or wav file from "./bard_songs"
    python jukebox.py --sound "metal_dragon_battle.mp3" --folder "./bard_songs" --> plays "metal_dragon_battle.mp3" if found in "./bard_songs"
    python jukebox.py --set-default-sound-folder "C://Music/Game_Tracks/Custom" --> returns success message or fail message
    python jukebox.py --get-default-sound-folder                                --> returns "C://Music/Game_Tracks/Custom" (if run after above example)

Citations:

Actual sound playing functionality provided by ["playsound" pypi plugin](https://pypi.org/project/playsound/): "Pure Python, cross platform, single function module with no dependencies for playing sounds."
