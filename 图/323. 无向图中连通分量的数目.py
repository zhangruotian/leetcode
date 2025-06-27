from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        cur_nodes = set(g.keys())
        res = n-len(cur_nodes)
        while cur_nodes:
            stack = []
            visited = set()
            start = next(iter(cur_nodes))
            stack.append(start)
            visited.add(start)
            while stack:
                popped = stack.pop()
                cur_nodes.remove(popped)
                for node in g[popped]:
                    if node not in visited:
                        stack.append(node)
                        visited.add(node)
            res+=1
        return res

# 从一个node出发，traverse，这次到达的所有节点组成一个land。然后找一个从未到达的node重新出发，traverse。最终所有node会被走完，记录一共出发了几次。
# 注意孤立的node，没有任何信息在edges list里面，需要在res中把它们加上。
