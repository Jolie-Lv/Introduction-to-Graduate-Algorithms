#euclid.py
x= 25
y = 15
from math import floor
def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)
print (GCD(x, y))
def ExtEuclid(x, y):
    if y == 0:# d = x,d= a*x + y *b, 1 = a*x+ b*y b =
        d=x
        a=1
        b=0
        return d, a, b
    d, ap, bp  = ExtEuclid(y, x%y)
    return d, bp, ap - floor(x/y)*bp
d, a, b = ExtEuclid(x, y)
print(d, a, b)
 
    
