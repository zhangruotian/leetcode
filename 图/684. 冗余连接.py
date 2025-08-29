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
        for node1,node2 in edges:
            is_united=self.union(parents,node1,node2)
            if not is_united:
                return [node1,node2]

    def find(self,parents,index):
        if parents[index]==index:
            return index 
        root = self.find(parents,parents[index])
        parents[index] = root
        return root
    
    def union(self,parents,index1,index2):
        root1 = self.find(parents,index1)
        root2 = self.find(parents,index2)
        if root1==root2:
            return False
        parents[root1]=root2 
        return True
# union find并查集 https://www.youtube.com/watch?v=VJnUwsE4fWA 
# https://leetcode.cn/problems/redundant-connection/solutions/181093/tong-su-jiang-jie-bing-cha-ji-bang-zhu-xiao-bai-ku/
