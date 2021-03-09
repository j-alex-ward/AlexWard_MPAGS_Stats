import numpy

P_Infected = 0.002
P_NotInfected = 1 - P_Infected
P_Positive_Giv_Infect = 0.99
P_Positive_Giv_NotInfect = 0.0015

P_PositiveANDInfected = P_Infected * P_Positive_Giv_Infect
P_PositiveANDNotInfected = P_NotInfected * P_Positive_Giv_NotInfect

P_PositiveTest = P_PositiveANDInfected + P_PositiveANDNotInfected

P_Infected_Given_PositiveTest = P_Positive_Giv_Infect * ( P_Infected / P_PositiveTest )

print("P( Infected | Positive Test ) = {}".format(P_Infected_Given_PositiveTest))