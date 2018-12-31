#convertGraphObject.py
#creates a graph object and converts it to a graph array

INF = float("Inf")
class Graph:
    def __init__(self,vertices):
        self.V = vertices #No. of vertices
        self.graph = [] 
    #u-origin vertex/node
    #v-destination vertex/node
    #w-distance
    def addEdge(self,u,v,w):
        self.graph.append([u, v, w])

def printArray(dist,V): 
    for i in range(V): 
        for j in range(V): 
            if(dist[i][j] == INF): 
                print ("%7s\t" %(dist[i][j]),end="")
            else: 
                print ("%7d\t" %(dist[i][j]),end="")
            if j == V-1: 
                print ("")


"""
#graph array
graph = [
        [0, 3,   INF, 7], 
        [ 8, 0,   2,   INF], 
        [ 5, INF, 0,   1], 
        [ 2, INF, INF, 0] 
        ]
printArray(graph)
"""
g = Graph(6)
print("creating graph object")
g.addEdge(0, 1, 5)
g.addEdge(1, 2, 3) 
g.addEdge(2, 3, -6)
g.addEdge(2, 4, 4)
g.addEdge(3, 1, 2)
g.addEdge(3, 6, 5)
N=6

def convertGraphObject(graphObject):
    graphArray = [[INF for i in range(N+1)]for i in range(N+1)]
    for i in range(N):
        graphArray[i][i] = 0
    print("vertex\tvertex\tdist")
    print("from\tto\tdist")       
    for i in range(N):
        u,v, w = graphObject[i]
        print ("%d\t%d\t%d" % (u,v, w))
        graphArray[u][v] = w
    print("\ngraph as array")
    printArray(graphArray,N)
    return graphArray
    
convertGraphObject(g.graph)
