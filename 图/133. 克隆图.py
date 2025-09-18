"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        q = deque([node])
        visited = {node.val:Node(node.val)}
        while q:
            popped = q.popleft()
            for neighbor in popped.neighbors:
                if neighbor.val in visited:
                    visited[popped.val].neighbors.append(visited[neighbor.val])
                    continue
                q.append(neighbor)
                new_node = Node(neighbor.val)
                visited[neighbor.val] = new_node
                visited[popped.val].neighbors.append(new_node)
        return visited[1]
# bfs traverse的途中创建克隆节点
# 要在入队的时候添加connect，因为出队的时候拿不到它之前的那个node。
# 单向添加关系+如果某个neighborvisited不立马continue， 使代码更简单。


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        visited = {}
        new_node_prev = Node()
        self.dfs(node,new_node_prev,visited)
        return visited[1]

    def dfs(self,ori_node,new_node_prev,visited):
        if ori_node.val in visited:
            visited[ori_node.val].neighbors.append(new_node_prev)
            return
        new_node = Node(ori_node.val)
        visited[ori_node.val]=new_node
        if new_node_prev.val!=0:
            new_node.neighbors.append(new_node_prev)
        for neighbor in ori_node.neighbors:
            self.dfs(neighbor,new_node,visited)
# dfs traverse的途中创建克隆节点
# 记录上个created的node，使得当前new node能跟之前的建立联系
# 单向添加关系+如果某个neighborvisited不立马return，使代码更简单。
