#prob6.4 Knapsack
#repetition
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
K = [0 for j in range(B+1)] 
#prString(K, n+1, B+1)
#solution total value v=8 + v=10 -> 18
#total weight 22 w=12+ w=10 -> 22
#order O(nB)
def findMax(w, v):
    n = len(v)
    
    for b in range(1, B+1):
            
                #use all v[i]s
                for i in range(1, n):
                    if w[i] <= b:
                        K[b] = max(K[b], v[i]+K[b-w[i]])
                    else:
                        K[b] = K[b]

    print(" total values = \n")
    print ( K)

    print ("max total value = ", K[B])
findMax(w, v)
    
    
