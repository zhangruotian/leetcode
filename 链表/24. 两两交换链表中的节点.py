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
# ！！！！！！！！！！！！！！反转链表套路：        
# 虚拟头结点
# 在循环外定义pre cur，在循环内求next和next_next(如果有需要)，这样就可以cur and cur.next作为判断while条件
