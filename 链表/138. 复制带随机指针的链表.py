"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        cur = head
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            new_node = d[cur]
            if cur.next:
                new_node.next = d[cur.next]
            if cur.random:
                new_node.random = d[cur.random]
            cur=cur.next
        return d[head] if d else None

# Pass 1: Create Nodes & Map:
# Create a hash map, let's call it old_to_new_map.
# Iterate through the original list. For each old_node, create a new_node with the same value.
# Store the mapping: old_to_new_map[old_node] = new_node.

# Pass 2: Assign Pointers:
# Iterate through the original list again.
# For each old_node:
# Get its copy: new_node = old_to_new_map[old_node].
# Set the next pointer: new_node.next = old_to_new_map.get(old_node.next). Using .get() handles the case where old_node.next is None.
# Set the random pointer: new_node.random = old_to_new_map.get(old_node.random).
