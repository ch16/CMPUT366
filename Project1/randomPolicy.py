import blackjack
import numpy as np
from pylab import *

numEpisodes = 2000

def policy(s):
    return np.random.randint(2)

returnSum = 0.0
for episodeNum in range(numEpisodes):
    G = 0
    
    print "Episode: ", episodeNum, "Return: ", G
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes
