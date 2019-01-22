#multPoly
import numpy as np
from scipy.fftpack import fft, ifft
a = [1,2,3]
b = [2,-1,4]
#reserve space for the product
prod =[0 for i in range(len(a)+len(b)-1)]
for i in range(len(a)):
    for j in range(len(b)):
        prod[i+j] += a[i]*b[j]

#print (prod)
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5,0])
    
y = np.array(fft(a))
print (y)
yinv = ifft(y)
print (yinv)

import numpy as np
def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)
y = DFT_slow(x)
print (y)

def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        print ("factor",factor)
        return np.concatenate([X_even + factor[:N / 2] * X_odd,
                               X_even + factor[N / 2:] * X_odd])
print (FFT(x))
y = DFT_slow(x)
print (y)
a = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print (a[::2])
