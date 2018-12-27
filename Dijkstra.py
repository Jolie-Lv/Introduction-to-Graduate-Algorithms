#Dijkstra.py
# Python program for Dijkstra's algo 
INF = float("Inf") 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices#number of vertices 
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)] 

    def printSolution(self, dist): 
        print ("Vertex \tDistance")
        for node in range(self.V): 
            print (node,"\t",dist[node] )

 
    # find the vertex with min distance not visited yet 
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
        #print("sptSet=",sptSet)
        # Initilaize minimum distance for next node 
        minD = INF
        min_index=0
        # shorest dist not in shortest path tree (sptSet[v])
        for v in range(self.V): 
            if dist[v] < minD and sptSet[v] == False: 
                minD = dist[v] 
                min_index = v 

        return min_index 

    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation 
    def dijkstra(self, src): 

        dist = [INF] * self.V
        
        dist[src] = 0
        sptSet = [False] * self.V 

        for cout in range(self.V):
            print("distances ",dist,"at iteration",cout)

            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 

            # Put the minimum distance vertex in the 
            # shotest path tree 
            sptSet[u] = True

            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and\
                dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 

        self.printSolution(dist) 

# Driver program 
g = Graph(6)
"""
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ];
"""
g.graph =[
        #1     2   3    4   5     6
        [0,    2,  4, INF,  INF, INF], #1
        [INF,  0,  1,   7,  INF, INF], #2
        [INF,  8,  0, INF,    3, INF], #3
        [INF,INF,INF,   0,  INF,   1], #4
        [INF,INF,INF,   2,    0,   5], #5
        [INF,INF,INF, INF,  INF,   0], #6
        
        ];
g.graph =[
        #1     2   3    4   5     6
        [0,    50,  45, 10,  INF, INF], #1
        [INF,  0,  10,   15,  INF, INF], #2
        [INF,  INF,  0, INF,    30, INF], #3
        [10,INF,INF,   0,  15,   INF], #4
        [INF,20,35,   INF,    0,   INF], #5
        [INF,INF,INF, INF,  3,   0], #6
        
        ];
g.printSolution(g.graph)
g.dijkstra(0); 

# This code is contributed by Divyanshu Mehta 

