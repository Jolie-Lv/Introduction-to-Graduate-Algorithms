#rsa
import random
from math import floor
def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

def ExtEuclid(x, y):
    if y == 0:# d = x,d= a*x + y *b, 1 = a*x+ b*y b =
        d=x
        a=1
        b=0
        #print(d, a, b)
        return d, a, b
    d, ap, bp  = ExtEuclid(y, x%y)
    #print(d, ap, bp)
    return d, bp, ap - floor(x/y)*bp

def encrypt(m):

    lst = [3,5,7,11]
    gcd = 0
    i=0
    while gcd != 1:
        p = int(random.random()*1000)
        q = int(random.random()*1000)
        if i >= len(lst):
            i=0
        e = lst[i]
        gcd = GCD((p-1)*(q-1), e)         
        print("trying e= ", e, "gcd =",gcd, "i=",i)
        i=i+1

    rslt = ExtEuclid((p-1)*(q-1), e)
    d = rslt[2]
    N = p*q
    print ("N, e =", N, e)
    #private key
    print ("p, q, e  =",p, q, e)
encrypt(1)
