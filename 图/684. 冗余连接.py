from collections import defaultdict,deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = [0]*len(edges)
        q = deque()
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
            indegrees[e-1]+=1
            indegrees[s-1]+=1

        for i in range(len(indegrees)):
            if indegrees[i]==1:
                q.append(i+1)
        while q:
            popped = q.popleft()
            for child in graph[popped]:
                indegrees[child-1]-=1
                if indegrees[child-1]==1:
                    q.append(child)

        for i in range(len(edges)-1,-1,-1):
            s,e=edges[i]
            if indegrees[s-1]==2 and indegrees[e-1]==2:
                return edges[i]
# topological sort，从indegree为1的开始。如果有环，环上的node的indegree最终都是2。
