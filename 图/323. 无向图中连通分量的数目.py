from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = [0]*n
        res = 0
        for start in range(n):
            if visited[start]:
                continue
            res+=1
            if start in graph:
                self.dfs(graph,start,visited)
        return res
    
    def dfs(self,graph,node,visited):
        if visited[node]:
            return
        visited[node] =1
        for child in graph[node]:
            self.dfs(graph,child,visited)
# DFS
# 从一个node出发，traverse，这次到达的所有节点组成一个land。然后找一个从未到达的node重新出发，traverse。最终所有node会被走完，记录一共出发了几次。
# 注意孤立的node，没有任何信息在edges list里面，需要在res中把它们加上。

from collections import defaultdict,deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
        visited = [0]*n
        res = 0
        q = deque()
        for start in range(n):
            if visited[start]:
                continue
            q.append(start)
            visited[start]=1
            while q:
                popped = q.popleft()
                for child in graph[popped]:
                    if not visited[child]:
                        q.append(child)
                        visited[child]=1
            res+=1
        return res
#BFS
