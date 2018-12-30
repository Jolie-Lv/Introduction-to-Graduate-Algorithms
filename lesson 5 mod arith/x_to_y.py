#RCS_x_to_y
from math import floor
N = 23
y = 5
x = 7
print ("(x**y)%N = ",(x**y)%N)

D=[0 for i in range(20)]
def mod_exp(x,y,N):
    if y == 0:
        return 1
    z = mod_exp(x, floor(y/2), N)
    if y%2 == 0:#y is even
        return ( z*z )% N
    else:
        return ( x*z*z )% N
z = mod_exp(x,y,N)
print (z)

            
            
        
        
