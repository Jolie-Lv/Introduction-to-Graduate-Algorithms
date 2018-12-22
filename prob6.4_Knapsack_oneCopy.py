#prob6.4 Knapsack
#one copy
def prString(myStr, n, B):
    n = n
    m = B
    print(' ',end="")
    for j in range(0, m):
        print("{0:3d}".format(j),end="")
        #print (j,' ',end="")
    print()
        
    for i in range(0, n):
        print(i,end="")
        for j in range(0, m):
            print("{0:3d}".format(myStr[i][j]),end="")
        print()

v=[0,15,10,8,1]
w=[0,15,12,10,5]
B=22
n = len(v)
K = [[0 for j in range(B+1)] for j in range(n)]
#prString(K, n+1, B+1)
#solution total value v=8 + v=10 -> 18
#total weight 22 w=12+ w=10 -> 22
def findMax(w, v):
    n = len(v)
    for i in range(1, n):
        for b in range(1, B+1):
            if w[i] <= b:
                K[i][b] = max(v[i]+K[i-1][b-w[i]], K[i-1][b])
            else:
                K[i][b] = K[i-1][b]

    print(" total values = \n")
    prString ( K, n, B+1)

    print ("max total value = ", K[n-1][B])
findMax(w, v)
    
    
