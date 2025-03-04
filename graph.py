from collections import deque


class graph:
    def __init__(self):
        self.graph={}
    def addVertex(self,v):
        if  v not in self.graph:
            self.graph[v]=[]
    def addEdges(self,v1,v2):
        if v1 not in self.graph:
            self.addVertex(v1)
        if v2 not in self.graph:
            self.addVertex(v2)
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    
    def bfs(self,start):
        visited=set ()
        result=[]
        que=deque([start])
        while que:
            node=que.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                que.extend(self.graph[node])
        return result
            

        
            
        
    

g=graph()
g.addEdges('a','b')
g.addEdges('a','c')
g.addEdges('c','b')
g.bfs('a')
print(g.bfs('a'))


        