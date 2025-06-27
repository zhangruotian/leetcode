from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        prev = -1
        cur = 0
        visited = set()
        if not self.dfs(g,cur,prev,visited):
            return False
        print(visited)
        return len(visited)==n
    
    def dfs(self,g,cur,prev,visited):
        if cur in visited:
            return False
        visited.add(cur)
        for node in g[cur]:
            if node == prev:
                continue
            prev=cur
            if not self.dfs(g,node,prev,visited):
                return False
        return True
# 一个图是树必须满足两个充要条件：
# 1.图中无环 (Acyclic)
# 2.所有节点必须连通 (Fully Connected)

# undirected图中无环:
# dfs维护prev，用来组织dfs往回走。维护一个visited记录已经走过的node，如果当前的cur在visited中，证明有环。

# 所有节点必须连通：
# 从任意一个node开始，都能把全部的node visit一次。

# 补充：directed图中无环（207课程表）：
# 拓扑排序，从in degree为0的开始，依次遍历。走过一个node后，把这个node连接的node入度-1。遍历的时候只把入度为0的儿子加入。 最终如果所有node的入度都为0，则无环；否则有环。
