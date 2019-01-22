#quickSelect
A = [5,2,20,17,11,13,8,9,11]
def select(A, k):
    #print ("A=", A)
    n = len(A)
    if n == 1:
        return A[0]
    p=A[int(n/2)]
    ApMinus=[]
    ApPlus=[]
    Aeq=[]
    #print ("p=", p, "n=", n,"k=", k)
    for i in range(n):
        if A[i] < p:
            ApMinus.append(A[i])
        elif A[i] > p:
            ApPlus.append(A[i])
        else:
            Aeq.append(A[i])
    #print( ApMinus, Aeq, ApPlus)
    lenMinus = len(ApMinus)
    lenEq = len(Aeq)
    if k <= lenMinus:
        #search ApMinus
        return select(ApMinus, k)
    #found return p
    if  k <= (lenMinus+lenEq):
        return p
    #search ApPlus
    return select(ApPlus, k-lenMinus-lenEq)
    
        
print ("input array ", A)    
for i in range(1, len(A)+1):           
    print ("Kth smallest ",i, " is ", select(A, i))       
            
            
        
    
