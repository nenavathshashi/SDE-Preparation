from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def display(self):
        return self.graph
    def BfsRecursive(self,node,visited):
        visited.add(node)
        print(node)
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.BfsRecursive(neighbour,visited)
    def BfsIterative(self,node):
        q=deque()
        q.append(node)
        visited=set()
        while(q):
            vertex=q.popleft()
            if vertex in visited:
                continue
            print(vertex)
            visited.add(vertex)
            for neighbour in self.graph[vertex]:
                q.append(neighbour)
    def adj_to_dict(self,adj):
        for i in range(len(adj)):
            for j in range(len(adj[0])):
                if adj[i][j]==1:
                    self.graph[i].append(j)
        return self.graph
g=Graph()
#g.addEdge(0,1)
#g.addEdge(0,2)
##g.addEdge(0,3)
##g.addEdge(2,4)
##g.addEdge(3,3)
print(g.adj_to_dict([[0,1,1],[0,0,0],[0,0,0]]))
g.BfsRecursive(0,set())
g.BfsIterative(0)
