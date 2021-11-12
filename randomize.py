#!/usr/bin/env python3
import subprocess, random, glob

sounds = glob.glob('/Users/felix/Library/Sounds/audio/*.aiff')
sound = random.choice(sounds)
# print('randomly selected sound: ', sound)
command = 'defaults write .GlobalPreferences com.apple.sound.beep.sound {}'.format(sound)

subprocess.call(command, shell=True)