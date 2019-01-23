#roots of unity
#print the n roots of unity 

import math 

def printUnityRoots(n): 
 
    theta = math.pi * 2 / n 
    for k in range(0, n):
        print("root", k)

        # calculate the real and imaginary part of root 
        real = math.cos(k * theta)
        img = math.sin(k * theta) 

        # Print real and imaginary parts
        print("real\t  imaginary")
        print("%3f"%(real), end=" ") 
        if(img >= 0): 
            print("+", end="") 
        else: 
            print("-", end="") 
        print("%3f"%(abs(img)),"i")
        print("")


if __name__=='__main__': 
    printUnityRoots(8)#first 8 roots  
