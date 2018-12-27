#BellmanFord2.py
#Bellman Ford Algorithm - Single Source Shortest Path - Dynamic Programming
#Abdul Bari

INF = float("Inf")
n=7
d= [INF for c in range(n)]
c= [0 for c in range(n)]
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices#number of vertices 
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)] 

    def printSolution(self, dist): 
        #print ("Vertex \tDistance")
        for node in range(self.V): 
            print (node,"\t",dist[node] )



    def BellmanFord(self, src):
        n=self.V
        d = [INF] * self.V
        d[src] = 0
        #cost from u to v
        print("initial graph")
        print(d)
        #input("Press Enter to continue...")
        for k in range(n-1):
         for u in range(n):
            for v in range(n):
                c[u] = self.graph[u][v]
                #print ("c=", c)
                if d[u] + c[u] < d[v]:
                    d[v] = d[u] + c[u] 

            print("node",u, " d = ",d)
            #input("Press Enter to continue...")

# Driver program 
g = Graph(7)


g.graph =[
        #1     2   3   4   5   6   7
        [0,    6,  5,  5,INF, INF,INF], #1
        [INF,  0,INF,INF,-1, INF,INF], #2
        [INF, -2,  0, INF,1, INF,INF], #3
        [INF,INF, -2,   0,INF,-1,INF], #4
        [INF,INF,INF,   INF,    0,INF,3], #5
        [INF,INF,INF, INF,INF,   0, 3], #6
        [INF,INF,INF, INF,INF,   INF, 0], #7
        
        ];
g.printSolution(g.graph)
g.BellmanFord(0); 

# This code is contributed by Divyanshu Mehta 

