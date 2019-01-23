#evaluatePoly
import math
import numpy as np
a = [3,2,5]
#3*x**2 + 0*x + 1
def evalA(a, x ):
    rslt =   np.polyval(a, x)
    return rslt
print (evalA(a, 0 )) #5 =  3*0**2 + 2*0 + 5
print (evalA(a, 2 )) #21 =  3*2**2 + 2*2 + 5 = 12 +4 +5 = 21
print (evalA(a, 3 ))#38

#given a poly with the order n is even in this case n = 6
b = [3, 2, 5,7,9,1,4]
def splitEvenPoly(x):
    return x[::2]
 
def splitOddPoly(x):
    return x[1::2]
print ("poly=", b)
print ("odd  coeff = ", splitOddPoly(b))
print ("even coeff = ",splitEvenPoly(b))#coeff of even exponents:
