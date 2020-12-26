# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur=head
        pre=None
        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        return pre
        
        
        
# ！！！！！！！！！！！！！！反转链表套路：        
# 虚拟头结点
# 在循环外定义pre cur，在循环内求next和next_next(如果有需要)，这样就可以cur and cur.next作为判断while条件