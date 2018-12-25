#prob6.4 Knapsack
#one copy
w = [6, 3, 4, 2]#weights
v = [30,14,16,9]#values
B = 10#capacity
#v=[15,10,8,1]
#w=[15,12,10,5]

#B=22
#solution w6-v30 + w4-v16  = 46

def findMax(w, v):
    n = len(v)
    valPerWeight= [float(v[i]/w[i]) for i in range(n)]
    print (valPerWeight)
    S = []
    wt=0
    L=len(valPerWeight)
    while  L != 0:
        i = valPerWeight.index(max(valPerWeight))
        if wt+w[i] <=B :
            wt+=w[i]
            S.append(valPerWeight[i])
            print("i=",i,"wt=", wt,"val=", sum(S))
        valPerWeight.remove(valPerWeight[i])
        
        L=len(valPerWeight)
        #print("i=",i,"wt=", wt,"val=", sum(S))

    print (" using greedy approach")
    print (" total values = ", S)
    print (" total weight = ", wt)

findMax(w, v)
    
    
