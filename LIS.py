#LIS
#finds the longest in seq
#LIS longest in the sequence
#L array of number in the sequence
def findLIS():
    n = 11
    a = [5,7,4,-3,9,1,10,4,5,8,9,3]
    L = [i for i in range(0, n)]
    
    for i in range(0, n):
        L[i] = 1
        for j in range(0, i):
            if(a[j] < a[i] and (L[i] < 1 + L[j])):
                L[i] = 1 + L[j]

    print ("LIS = ", max(L))
    print ("L[]  = ",L)
    #input("Press Enter to continue...")
   
findLIS()
