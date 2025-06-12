"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        stack = [node]
        created = {}
        while stack:
            popped = stack.pop()
            if popped.val not in created:
                cloned = Node(val=popped.val)
                created[cloned.val] = cloned
            else:
                cloned = created[popped.val]

            for neighbor in popped.neighbors:
                if neighbor.val not in created:
                    stack.append(neighbor)
                    cloned_neighbor = Node(val=neighbor.val)
                    created[neighbor.val] = cloned_neighbor
                else:
                    cloned_neighbor = created[neighbor.val]
                cloned.neighbors.append(cloned_neighbor)

        return created[1]
      # traverse的途中创建克隆节点


