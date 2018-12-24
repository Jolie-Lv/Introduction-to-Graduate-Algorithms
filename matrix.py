#matrix
n = 10
m = 10
C = [[0 for i in range(n)]for i in range(n)]
S=[0 for i in range(n)]
def prString(myStr):

    print("{0:5d}".format(0),end="")
    for j in range(0, m):
        print("{0:5d}".format(j),end="")
    print()
    for i in range(0, n):
        print("{0:5d}".format(i), end="")
        for j in range(0, m):
            print ("{0:5d}".format(myStr[i][j]),end="")
        print()
            
def findMinCost():
    for i in range(0,n):
        C[i][i] = 0
    for s in range(0, n-1):
        for i in range(0, n-s):
            j = i+s
            C[i][j]=100
        #print(i)
    prString(C)
  
    

findMinCost()
