#LCS
#longest common sequence in strings x and y
#L[i,j] length of LCS in xi, yj

#format the output of table L[][]  
def prString(myStr, x, y):
    n = len(x)
    m = len(y)
    print ('  ', y)
    print( '  ',end="")
    for j in range(0, m+1):
        print(0,end="")
    print()
    for i in range(0, n):
        print(x[i], 0,end="")
        for j in range(0, m):
            print (myStr[i][j],end="")
        print()
            
def findLCS():
    x = "BCDBCDA"
    y = "ABECBA"
    m = len(y)
    n = len(x)
    L = [[0 for j in range(0, m)] for i in range(0, n)]

    for i in range(0,n):
        for j in range(0,m):
            #print(i, j)
            if x[i] == y[j]:
                L[i][j] = 1+L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    print ("LCS = ", L[n-1][m-1])               
    prString (L, x, y)
    
findLCS()
        
    
