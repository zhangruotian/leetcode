"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:return head
        hashmap={}
        cur=head
        while cur:
            hashmap[cur]=Node(cur.val)
            cur=cur.next
        for ori_node,new_node in hashmap.items():
            ori_next=ori_node.next
            if not ori_next:
                new_node.next=None
            else:
                new_node.next=hashmap[ori_next]
            ori_random=ori_node.random
            if not ori_random:
                new_node.random=None
            else:
                new_node.random=hashmap[ori_random]
        return hashmap[head]
#hashmap
#https://www.youtube.com/watch?v=oXABtaRa37U