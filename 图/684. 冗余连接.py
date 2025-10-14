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


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(len(edges)+1))
        for s,e in edges:
            united = self.union(parents,s,e)
            if not united:
                return [s,e]
    
    def find(self,parents,node):
        if parents[node]==node:
            return node
        return self.find(parents,parents[node])
    
    def union(self,parents,node1,node2):
        parent1 = self.find(parents,node1)
        parent2 = self.find(parents,node2)
        if parent1==parent2:
            return False
        parents[parent1] = parent2
        return True
# union find并查集 https://www.youtube.com/watch?v=VJnUwsE4fWA 
# https://leetcode.cn/problems/redundant-connection/solutions/181093/tong-su-jiang-jie-bing-cha-ji-bang-zhu-xiao-bai-ku/
