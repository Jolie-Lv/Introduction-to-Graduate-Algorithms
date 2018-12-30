#6.1 max sum of contiguoius substring

a = [5,15,-30,10,-5,40, 10]

def findMCS(a):
    n = len(a)
    S=[0 for i in range(n)]

    for j in range(1, n):
        S[j] = max(0, a[j] + S[j-1])
    print ("S = ", S)
    print("MCS =", max(S))
findMCS(a)
    
