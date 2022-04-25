import sys
from time import sleep
from readchar import readchar

import numpy as np
from  pythagoras import PolyphonicPlayer

filename = sys.argv[1]

with open(filename, 'rb') as f:
    peaks, volumes = np.load(f)
volumes = volumes / np.sum(volumes)


print(len(peaks))
print(peaks)
print(volumes)


player = PolyphonicPlayer(base_freq=1, max_voices=len(peaks))
player.ratios = peaks
player.volumes = volumes
player.start()

readchar()
player.kill()
player.join()
