"""
jukebox.py
@author: codequiver (github.com/codequiver)

This script will play a random mp3 or wav sound file from a set folder when activated. 
By default, the folder is "./jukebox_sound".

Alternatively, a specific sound file name or a specific folder can be passed as argument(s).

The script can be called with the "--set-default-sound-folder" flag to change the source folder going forward.
This setting will be stored in `default_sound_folder.config`. (The "--folder" flag does *not* include this functionality.)

Args:
--sound                        Name of a specific sound file to play.
--folder                       Path to a specific folder to search for sound files, instead of the stored setting.
--set-default-sound-folder     Set a folder as the new default folder to search for sound files. Relative or absolute path both work.
--get-default-sound-folder     Print the current default sound folder stored in `default_sound_folder.config`, then exit script.

Sample Usage:
    python jukebox.py                                                           --> randomly play an mp3 or wav file from the default folder
    python jukebox.py --sound "metal_dragon_battle.mp3"
    python jukebox.py --folder "./bard_songs"
    python jukebox.py --sound "metal_dragon_battle.mp3" --folder "./bard_songs"
    python jukebox.py --set-default-sound-folder "C://Music/Game_Tracks/Custom" --> returns success message or fail message
    python jukebox.py --get-default-sound-folder                                --> returns "C://Music/Game_Tracks/Custom"
"""

# (NOTE- ctrl+d exits iPython process when done using it)

import sys
import os
import argparse
import random
import IPython  # optional, for development
from playsound import playsound

# constants to never be overwritten
default_sound_folder = "./jukebox_sound"
setting_file = "default_sound_folder.config"

# if there's a saved setting already in existence, override the value with that
if os.path.exists(setting_file):
    with open(setting_file) as f:
        data = f.read()
        # below checks for 0 length/empty or None
        if data:
            default_sound_folder = data

# var to use ongoing in script
# sound_folder = default_sound_folder


def parse_args(raw_args):
    """
    Get the args that the user passed in.
    """
    parser = argparse.ArgumentParser(
        description="play a sound with certain parameters, defaults to random sound in ./jukebox_sound folder"
    )
    parser.add_argument(
        "--sound",
        dest="chosen_sound",
        help="Name of a specific sound file to play, instead of randomly selecting on in the folder.",
    )
    parser.add_argument(
        "--folder",
        dest="sound_folder",
        default=default_sound_folder,
        help="Path to a specific folder to search instead of the stored setting.",
    )
    parser.add_argument(
        "--set-default-sound-folder",
        dest="set_default_sound_folder",
        help="Path to a specific folder to store as the new default.",
    )
    parser.add_argument(
        "--get-default-sound-folder",
        action="store_true",
        dest="get_default_sound_folder",
        help="Returns the name of the current default sound folder per the settings.",
    )

    args = parser.parse_args(raw_args)
    print(args)

    return args


def update_default_folder(new_folder):
    """
    if setting_file file doesn't exist, create it
    write the new value to the file
    ('w' setting means it will create a new file if needed, or open an existing one)
    """
    global setting_file

    with open(setting_file, "w") as f:
        f.write(new_folder)


def play_random_sound(folder):
    mp3_and_wav_files = [
        file
        for file in os.listdir(folder)
        if (file.endswith(".mp3") or (file.endswith(".wav")))
    ]
    targ_sound = random.sample(mp3_and_wav_files, 1)[0]
    targ_sound_path = f"{folder}/{targ_sound}"
    # print('playing sound', targ_sound_path)
    playsound(targ_sound_path)
    # IPython.embed();


def main(raw_args):
    global default_sound_folder
    sound_folder = default_sound_folder

    if len(raw_args) == 0:
        # no extra flags or settings, just default random
        print("run default settings- random sounds from default file")
        play_random_sound(sound_folder)
    else:
        # flags etc. included so parsing is necessary
        print("User passed some flags")
        args = parse_args(raw_args)

        if args.get_default_sound_folder:
            return default_sound_folder

        if args.set_default_sound_folder:
            try:
                update_default_folder(args.set_default_sound_folder)
            except (IOError, Exception) as e:
                print(
                    f"Failed to update default sound folder to '{args.set_default_sound_folder}'; Error: '{e}'"
                )
                raise
            print(
                f"Successfully updated default sound folder to '{args.set_default_sound_folder}'"
            )

        if args.sound_folder:
            sound_folder = args.sound_folder

        chosen_sound = args.chosen_sound
        if chosen_sound:
            print("playing sound", f"{sound_folder}/{chosen_sound}")
            playsound(f"{sound_folder}/{chosen_sound}")
            # IPython.embed()
        else:
            play_random_sound(sound_folder)


if __name__ == "__main__":
    result = main(sys.argv[1:])

    # print any return values to console
    if result:
        print(result)
