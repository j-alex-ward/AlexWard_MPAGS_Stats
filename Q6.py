import scipy.integrate as integrate
import math
import numpy as np

expMean = 28
measuredEvts = 48
poissonSigma = math.sqrt(expMean)

def Function(x):
    function = ( 1 / (poissonSigma*math.sqrt(2*math.pi))) * math.exp( -(x-expMean)**2 / (2*poissonSigma**2) )
    return function

def PerfectFunction(x):
    function = ( 1 / (math.sqrt(2*math.pi))) * math.exp( -(x)**2 / (2) )
    return function

def OLDconfidence(ConfidenceLevel = 1):
    '''One-tailed excess confidence, eg between limits -infitniy, n'''
    NSigmaMeasuredValue = round((measuredEvts - expMean) / poissonSigma ,2)
    upperIntegrationLimit = expMean + poissonSigma*NSigmaMeasuredValue
    #print(upperIntegrationLimit)
    P_ValWithinNSigma_InBin = integrate.quad(Function, -np.inf, upperIntegrationLimit)[0]
    Percent_ValWithinNSigma_InBin = round(P_ValWithinNSigma_InBin * 100 ,4)

    P_ValWithinNSigma_InBin_Pow = integrate.quad(Function, -np.inf, upperIntegrationLimit)[0]**84
    P_AtLeastOneNSigmaEffect_Pow = 1 - P_ValWithinNSigma_InBin_Pow
    Perc_AtLeastOneNSigmaEffect_Pow = P_AtLeastOneNSigmaEffect_Pow*100

    #P_ValWithinNSigma_InBin = integrate.quad(Function, -np.inf, ConfidenceLevel)[0]
    P_AllWithinNSigma = integrate.quad(PerfectFunction, -np.inf, ConfidenceLevel)[0]
    Perecntage_AllWithinNSigma = P_AllWithinNSigma*100
    P_AllWithinNSigma_PowNBins = P_AllWithinNSigma**84
    P_AtLeastOneNSigmaEffect = 1 - P_AllWithinNSigma_PowNBins
    Percent_AtLeastOneNSigmaEffect = P_AtLeastOneNSigmaEffect*100
    Failed_Prob = 1 - P_AllWithinNSigma
    Failed_Percentage = Failed_Prob*100

    print("\nUsing a one-tailed Poisson confidence integral for 84 bins (measurements):")
    print("Measured Value x = {0} is +{1} Sigma from Mean = {2}".format(measuredEvts, NSigmaMeasuredValue, expMean) )
    print("This has a probability of {1} = {0}%".format(Percent_ValWithinNSigma_InBin, round(P_ValWithinNSigma_InBin , 6) ))
    print("P(at least one increase of 20 events) = 1 - P(all within 20 event increase)^84 = {0}%".format(round(Perc_AtLeastOneNSigmaEffect_Pow,6) )  )
    #print("P(all within {0} Sigma) = {1}".format( ConfidenceLevel , round(P_AllWithinNSigma,8) ) )
    #print("P(at least one {0} Sigma effect) = 1 - P(all within {0} Sigma)^84 = {1}%".format( ConfidenceLevel , round(Percent_AtLeastOneNSigmaEffect,6) )  )
    print("x Value for {0} Sigma = {1}".format(ConfidenceLevel, round(ConfidenceLevel*poissonSigma + expMean ,2) ))
    #print("\n{1} Sigma Discovery Claim Confidence = P(All within {1}Sigma) = {2} = {0}%".format(Perecntage_AllWithinNSigma, ConfidenceLevel, P_AllWithinNSigma) )
    #print("False Discovery Claim = 1 - {1} = {0}%".format(Failed_Percentage, P_AllWithinNSigma) )
    #print("The probability to claim a false discvovery with these mesasurement is:")
    #print("P(At least one {2}Sigma effect) = 1 - P(All within {2}Sigma)^84 = {0} = {1}%".format(P_AtLeastOneNSigmaEffect , Percent_AtLeastOneNSigmaEffect, ConfidenceLevel) )
    #print("With an expected mean = 28, the {1}Sigma limit = {0}".format(SigmaVal(ConfidenceLevel), ConfidenceLevel), "\nThe Measured value is therefore {0} higher than the {1}Sigma confidence value".format(xValue(48, ConfidenceLevel), ConfidenceLevel))
    return


def confidence():
    '''One-tailed excess confidence, eg between limits -infitniy, n'''
    NSigmaMeasuredValue = round((measuredEvts - expMean) / poissonSigma ,2)
    upperIntegrationLimit = expMean + poissonSigma*NSigmaMeasuredValue
    P_ValWithinNSigma_InBin = integrate.quad(Function, -np.inf, upperIntegrationLimit)[0]
    Percent_ValWithinNSigma_InBin = round(P_ValWithinNSigma_InBin * 100 ,4)
    P_ValWithinNSigma_InBin_Pow = integrate.quad(Function, -np.inf, upperIntegrationLimit)[0]**84
    P_AtLeastOneNSigmaEffect_Pow = 1 - P_ValWithinNSigma_InBin_Pow
    Perc_AtLeastOneNSigmaEffect_Pow = P_AtLeastOneNSigmaEffect_Pow*100
    
    print("\nUsing a one-tailed Poisson confidence integral for 84 bins (measurements):")
    print("Measured Value x = {0} is +{1} Sigma from Mean = {2}".format(measuredEvts, NSigmaMeasuredValue, expMean) )
    print("This has a probability of {1} = {0}%".format(Percent_ValWithinNSigma_InBin, round(P_ValWithinNSigma_InBin , 6) ))
    print("P(at least one increase of 20 events) = 1 - P(all within 20 event increase)^84 = {0}%".format(round(Perc_AtLeastOneNSigmaEffect_Pow,6) )  )
    print("x Value for 3 Sigma = {0}".format(round(3*poissonSigma + expMean ,2) ))
    print("x Value for 5 Sigma = {0}".format(round(5*poissonSigma + expMean ,2) ))
    return

confidence()