#easy D and C

def printBin(a, pad=4):
    b = '{:b}'.format(a)
    if len(b) % pad:
        b = '0' * (pad - (len(b) % pad)) + b
    return ' '.join(b[k:k+pad] for k in range(0, len(b), pad))


def debug(n, x, y, mask, xL,xR,yL,yR):
    print("n=", n)
    print('x=',printBin(x))
    print('y=',printBin(y))
    print('mask =',printBin(mask))

    print('xl=',printBin(xL))
    print('xR=',printBin(xR))
    print('yl=',printBin(yL))
    print('yR=',printBin(yR))
    #input("hit enter to continue")

def EasyMult(x, y, n):

    if n == 1:
        c = x & y
        #print(c)
        return c
    width = int(n/2)

    mask = (1 << width) - 1
    
    xL = x >> int(n/2)
    xR = x & mask
    yL = y >> int(n/2)
    yR = y & mask

    n2 = int(n/2)
    A = EasyMult(xL, yL,n2)
    B = EasyMult(xR, yR,n2)
    C = EasyMult(xL, yR,n2)
    D = EasyMult(xR, yL,n2)
    
    Z = (2**n)*A + (2**n2) * (C+D) + B
    return Z

x= 130
y = 55
print("x*y = ", x*y)
n = 32
print (EasyMult(x, y, n ))
