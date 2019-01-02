#multPoly
a= [1,2,3]
b=[2,-1,4]
prod =[0 for i in range(len(a)+len(b)-1)]
for i in range(len(a)):
    for j in range(len(b)):
        prod[i+j] += a[i]*b[j]

print (prod)
