#LCS_sequence
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
    L = [[0 for j in range(0, m+1)] for i in range(0, n+1)]

    for i in range(0,n):
        for j in range(0,m):
            #print(i, j)
            if x[i] == y[j]:
                L[i][j] = 1+L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    

    #print ("LCS = ", L[n-1][m-1])               
    #prString (L, x, y)
    
    return L
    
#input("Press Enter to continue...")
#solution: ABCB
def findSequence(L):
    x = "BCDBCDA"
    y = "ABECBA"
    seq =[]#holds the sequence of the common string
    m = len(y)
    n = len(x)
    i=n-1
    j=m-1
    end = L[i][j]#center diagonal of the L[] array
    #iterate through the array from the last element
    #to the first element
    #search the column for a match
    while end > 0:
        found = False
        startJ = j
        startI = i

        while  L[i][j] == end:
            if x[i] == y[j]:
                found = True
                break
            j=j-1
        j=startJ
        #search the row for a match
        while  not found and L[i][j] == end:
            if x[i] == y[j]:
                break
            i=i-1
        #if a match was found append it to the sequence
        if x[i] == y[j]:
            seq.append(x[i])
            print(x[i], y[j])       
        # go diagonally to the next element                 
        i=startI-1
        j=startJ-1
        end = L[i][j]
        
    print (seq)
    seq = seq[::-1]
    print ("sequence =",''.join(seq))
        
        
L = findLCS()
findSequence(L)
        
    
