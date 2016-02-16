
import numpy as np
def fft(x,y) :
    sampling_rate=150
    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/sampling_rate
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]
    return frq,Y