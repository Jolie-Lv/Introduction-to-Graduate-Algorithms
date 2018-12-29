#LCS_attempt1
#LCS
#L[i,j] length of LCS in xi, yj
def includes(LCS, x):
    if x in L:
        return True
    return False
    
def findLCS():
    x = "BCDBCDA"
    y = "ABECBABD"
    n = len(x)
    L = [0 for i in range(0, n)]
    LCS = []
    for i in range(n):
        for j in range(n):
            if x[i] == y[j]:
                L[i] = 1 + L[i-1]
                LCS.append(x[i])
            #elif x[i] != y[j]:
                #print (x[i], y[i])


    print (L)
    print (LCS)
findLCS()
        
    

