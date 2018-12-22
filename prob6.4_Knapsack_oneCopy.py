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

v=[15,10,8,1]
w=[15,12,10,5]
B=22
n = len(v)
K = [[0 for j in range(B)] for j in range(n)]
prString(K, n, B)
#solution w6-v30 + w4-v16  = 46
def findMax(w, v):
    n = len(v)
    #b total weight 
    
    
    for i in range(0, n):
        for b in range(0, B):
            capacity = B - w[i]
            
            if K[i][b] > capacity:
                continue
        
        K[i] = v[i] + v[i-1]

    print (" total values = ", K)

    print ("max total value = ", max(K))
findMax(w, v)
    
    
