import blackjack as bj
import numpy as np
from pylab import *

numEpisodes = 2000
returnSum = 0.0

num_states = 180
num_actions = 2

alpha = 0.001

Q =  0.00001*rand(num_states,num_actions)

for episodeNum in range(numEpisodes):
    G = 0
    s = bj.init()
    while s != -1:
        r, s = bj.sample(s,np.random.randint(2))
        G+=r
    
    print "Episode: ", episodeNum, "Return: ", G
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes

