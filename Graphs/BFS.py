from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def display(self):
        return self.graph
    def DfsRecursive(self,node,visited):
        visited.add(node)
        print(node,end=" ")
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.DfsRecursive(neighbour,visited)
    def DfsIterative(self,node):
        stack=deque()
        stack.append(node)
        visited=set()
        while(stack):
            vertex=stack.pop()
            if vertex in visited:
                continue
            print(vertex,end=" ")
            visited.add(vertex)
            for neighbour in self.graph[vertex]:
                stack.append(neighbour)

    def BfsIterative(self,node):
        q=deque()
        q.append(node)
        visited=set()
        while(q):
            vertex=q.popleft()
            if vertex in visited:
                continue
            print(vertex,end=" ")
            visited.add(vertex)
            for neighbour in self.graph[vertex]:
                q.append(neighbour)
    def BfsRecursive(self,q,visited):
        #print("entered",len(q),q)
        if len(q)==0:
            return
        vertex=q.popleft()
        if vertex not in visited:
            print(vertex,end=" ")
            visited.add(vertex)
            for neighbour in self.graph[vertex]:
                q.append(neighbour)
            self.BfsRecursive(q,visited)

    def adj_to_dict(self,adj):
        for i in range(len(adj)):
            for j in range(len(adj[0])):
                if adj[i][j]==1:
                    self.graph[i].append(j)
        return self.graph
    def connectedComponents(self,vertices,visited):
        count=0
        for i in range(vertices):
            if i not in visited:
                visited.add(i)
                count+=1
                self.DfsRecursive(i,visited)
                print()
        return count
g=Graph()
#total vertices
V=10
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,7)
g.addEdge(7,8)
g.addEdge(2,4)
g.addEdge(5,6)
g.addEdge(9,9)
print(g.display())
#print(g.adj_to_dict([[0,1,1],[0,0,0],[0,0,0],]))
print("DFS in a Recursive approach:")
g.DfsRecursive(0,set())
print("\nDFS in a Iterative approach:")
g.DfsIterative(0)
print("\nBFS in a Iterative approach:")
g.BfsIterative(0)
q=deque()
q.append(0)
print("\nBFS in a Recursive approach:")
g.BfsRecursive(q,set())
print("\nDifferent connected components")
print("Total connected components:",g.connectedComponents(V,set()))
