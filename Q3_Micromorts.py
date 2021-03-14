from numpy import random

def numpyBin(MaxMiles):
    stepsize               = 6
    steps                  = int(MaxMiles/stepsize)    
    probOfAccidentEachStep = 1.e-6
    nExperiments = 100000
    x = random.binomial(n=steps, p=1-probOfAccidentEachStep, size=nExperiments)
    DeathChance = sum(x != steps) / nExperiments
    Perc_DeathChance = round(DeathChance*100,2)
    print("P(Die in {2} Mile Journey) = {0} = {1}%".format(DeathChance, Perc_DeathChance, MaxMiles) )
    return 0

numpyBin(15E3)
numpyBin(6E6)
numpyBin(6E7)