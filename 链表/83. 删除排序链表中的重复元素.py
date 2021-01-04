# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_node=ListNode(float(inf))
        dummy_node.next=head
        pre=dummy_node
        cur=head
        while cur:
            next=cur.next
            if pre.val==cur.val:
                pre.next=next
                cur=next
            else:
                pre=cur
                cur=next
        return dummy_node.next
# 模板：pre=dummy_node  cur=head  while cur:  next=cur.next