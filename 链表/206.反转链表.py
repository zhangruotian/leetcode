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
        
        
        
# 定义current。使用head迭代再无法找到头节点