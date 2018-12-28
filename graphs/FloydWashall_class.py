#Floyd Warshall Algorithm class

N= 4
V=4
INF = float("Inf")
A=[[0 for j in range(N)]for j in range(N)]
D=[[[INF for j in range(N)] for j in range(N)]for j in range(N)]
def printSolution(D): 
    print ("shortest distances between every pair of vertices" )
    for i in range(V): 
        for j in range(V): 
            if(D[i][j] == INF): 
                print ("%7s\t" %("INF"),end="")
            else: 
                print ("%7d\t" %(D[i][j]),end="")
            if j == V-1: 
                print ("")
def printD3(D): 
    for k in range(V): 
         for i in range(V): 
            for j in range(V): 
                if(D[k][i][j] == INF): 
                    print ("%7s\t" %(D[k][i][j]),end="")
                else: 
                    print ("%7d\t" %(D[k][i][j]),end="")
                if j == V-1: 
                    print ("")
         print ("")

def FloydWarshall(graph):
    for s in range(N):
        for t in range(N):
            w=graph[s][t]
            #print(w)
            if w != INF: #is edge
                #print(w)
                D[0][s][t] = w
                
            else:
                D[0][s][t] = INF
    #printD3(D)

    for i in range(1,N):
        for s in range(1,N):
            for t in range(1,N):
                #print(D[i-1][s][t], D[i-1][s][i], D[i-1][i][t])
                D[i][s][t] = min(D[i-1][s][t],D[i-1][s][i]+D[i-1][i][t])
                
                
    print("\n")
    #printD3(D)
    #input("cont.")
    #print(D[N-1])
    k=0#N-1 
    for i in range(V): 
        for j in range(V): 
            if(D[k][i][j] == INF): 
                print ("%7s\t" %(D[k][i][j]),end="")
            else: 
                print ("%7d\t" %(D[k][i][j]),end="")
            if j == V-1: 
                print ("")
    print ("")
    return D[N-1]
            


graph = [
        [0, 3,   INF, 7], 
        [ 8, 0,   2,   INF], 
        [ 5, INF, 0,   1], 
        [ 2, INF, INF, 0] 
        ]
#printSolution(graph)
FloydWarshall(graph)

