#RSA2
import random
from math import floor
global p, q
def mod_exp(x,y,N):
    if y == 0:
        return 1
    z = mod_exp(x, floor(y/2), N)
    if y%2 == 0:#y is even
        return ( z*z )% N
    else:
        return ( x*z*z )% N
def isPrime(r):
    #r = int(random.random()*1000)
    prime = 0
    for k in range(1,1000):
        Z = int(random.random()*(r-1)+1)
        prime = (Z**(r-1)) % r
        if prime != 1:
            return False
    return True

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)
def modinv(e, phi):
    for x in range(1, phi):
        if (e * x) % phi == 1:
            return x
    return None
def ExtEuclid(x, y):
    if y == 0:# d = x,d= a*x + y *b, 1 = a*x+ b*y b =
        return x,1,0
    d, ap, bp  = ExtEuclid(y, x%y)
    #print(d, ap, bp)
    z = int(x)/int(y)

    return d, bp, (ap - ( int( floor(x/y) )*bp))

def encrypt(m):
    global p, q

    lst = [3,5,7,11, 13, 17]
    gcd = 0
    i = 0
    while gcd != 1:
            p = int(random.random()*1000+1)
            q = int(random.random()*1000+1)
            if not isPrime(p) or not isPrime(q):
                continue
            e = lst[i]
            gcd = GCD(e,((p-1)*(q-1)))
            i=i+1
            if i >= len(lst):
                i=0
    N = p*q
    return N, e

def sendMsg(m,N,e):
    y= mod_exp(m,e,N)#using fast powers to do m**e
    y = m**e % N
    return y #encrypted message

def decrypt(y, N, e):
    global p, q
    phi = (p-1)*(q-1)
    ##############does not work##########
    rslt = ExtEuclid(phi,e)
    d = int(rslt[2])
    ####################################
    d = modinv(e, (p-1)*(q-1))
    m = (y**d) % N

    return m

def test():
    m= 123
    print("original msg = ", m)
    N, e = encrypt(m)
    y = sendMsg(m, N,e)
    print("encrypted msg = ", y)
    m = decrypt(y,N, e)
    print("decrypted msg = ", m)
def testExtEuclid():
    x = ExtEuclid(360, 7)
    d = int(x[2])#inverse of 7
    print ("7 inv =", d)
    print("?==1", d*7 %  360)
    print ()
    
def testIsPrime():
    print("Print the primes below 100") 

    for n in range(2, 100):
        x=isPrime(n)
        if(x):
            print (n, x)
def test1():
    e=17
    p=61
    q=53
    phi = (p-1)*(q-1)
    pq = 3233
    rslt = ExtEuclid(phi, e)
    print(rslt)
    d = int(rslt[2])
    d = modinv(e, phi)
    print(d)
    x  = (d*e) % ((p-1)*(q-1))
    print("d=1??", x)
    
if __name__=='__main__':

    testExtEuclid()
    testIsPrime()
    test()





    

