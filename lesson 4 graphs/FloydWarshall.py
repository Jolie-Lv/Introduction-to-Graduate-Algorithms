#Floyd Warshall Algorithm
N= 4
V=4
INF = float("Inf")
A=[[0 for j in range(N)]for j in range(N)]
def printSolution(dist): 
    print ("shortest distances between every pair of vertices" )
    for i in range(V): 
        for j in range(V): 
            if(dist[i][j] == INF): 
                print ("%7s\t" %("INF"),end="")
            else: 
                print ("%7d\t" %(dist[i][j]),end="")
            if j == V-1: 
                print ("")
def FloydWarshall(graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                A[i][j] = min(A[i][j], A[i][k]+A[k][j])


graph = [
        [0, 3,   INF, 7], 
        [ 8, 0,   2,   INF], 
        [ 5, INF, 0,   1], 
        [ 2, INF, INF, 0] 
        ]
printSolution(graph)
FloydWarshall(graph)
