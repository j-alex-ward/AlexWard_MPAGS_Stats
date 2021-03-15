import numpy as np
import math

print("Prob of one particle surviving by t=3tau = ",3*np.exp(-3))
'''
Using equation N=N_0 * e^(-kt)
'''
print("Probs of one of three particle surviving by t=3tau",3*np.exp(-3))

print("P(x) = e^(-a)*a*(x) / x! = ", (np.exp(-3) * 3**1 )/ math.factorial(1) )
'''
when starting with a=3 observed particles, the prob of having x observed particles at time t,
P(x) = e^(-a)*a*(x) / x!
'''