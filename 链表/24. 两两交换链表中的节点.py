# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head=ListNode(0)
        dummy_head.next=head
        pre=dummy_head
        cur=head
        while cur and cur.next:
            next=cur.next
            next_next=next.next
            pre.next=next
            next.next=cur
            cur.next=next_next
            pre=cur
            cur=next_next
        return dummy_head.next
        
# 虚拟头结点
# 定义pre cur next next_next