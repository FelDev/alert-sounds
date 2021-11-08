#!/usr/bin/env python3
import subprocess, random, glob
print('ehlala')

sounds = glob.glob('/Users/felix/Library/Sounds/*.aiff')
sound = random.choice(sounds)
print('randomly selected sound: ', sound)
command = 'defaults write .GlobalPreferences com.apple.sound.beep.sound {}'.format(sound)
# sounds=['tabarnak1', 'tabarnak2', 'tabarnak3']
# sound=random.choice(sounds)

# command = 'defaults write .GlobalPreferences com.apple.sound.beep.sound /Users/felix/Library/Sounds/{}.aiff'.format(sound)
# subprocess.call(' defaults write .GlobalPreferences com.apple.sound.beep.sound /System/Library/Sounds/Submarine.aiff ', shell=True)
subprocess.call(command, shell=True)
