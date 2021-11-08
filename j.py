#!/usr/bin/env python3
import subprocess, random, glob
print('HERE WE GO')

sounds = glob.glob('/Users/felix/Library/Sounds/*.aiff')
sound = random.choice(sounds)
print('randomly selected sound: ', sound)
command = 'defaults write .GlobalPreferences com.apple.sound.beep.sound {}'.format(sound)

# You could also define an array of sounds yourself, if you don't want every 
# .aiff file to be a possibility
# sounds=['tabarnak1', 'tabarnak2', 'tabarnak3']
# sound=random.choice(sounds)
# command = 'defaults write .GlobalPreferences com.apple.sound.beep.sound /Users/felix/Library/Sounds/{}.aiff'.format(sound)

subprocess.call(command, shell=True)