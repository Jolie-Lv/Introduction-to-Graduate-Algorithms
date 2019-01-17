#FastMultiply
#print a binary number for debug
def printBin(a, pad=4):
    b = '{:b}'.format(a)
    if len(b) % pad:
        b = '0' * (pad - (len(b) % pad)) + b
    return ' '.join(b[k:k+pad] for k in range(0, len(b), pad))

#print all variables
def debug(n, x, y, mask, xL,xR,yL,yR):
    print("n=", n)
    print('x=',printBin(x))
    print('y=',printBin(y))
    print('mask =',printBin(mask))

    print('xl=',printBin(xL))
    print('xR=',printBin(xR))
    print('yl=',printBin(yL))
    print('yR=',printBin(yR))
    #input("press enter to continue")

def FastMultiply(x, y, n):

    if n == 1:
        if y == 1:
            return x
        if x == 1:
            return y
        c = x * y
        return c
    width = int(n/2)

    mask = (1 << width) - 1 

    xL = x >> int(n/2)
    xR = x & mask
    yL = y >> int(n/2)
    yR = y & mask

    n2 = int(n/2)
    A = FastMultiply(xL, yL,n2)
    B = FastMultiply(xR, yR,n2)
    C = FastMultiply((xL+xR), (yL+yR),n2)
    
    Z = (2**n)*A + (2**n2) * (C-A-B) + B
    return Z

x= 11
y = 6
print("x*y = ", x*y)
n = 16
print (FastMultiply(x, y, n ))
