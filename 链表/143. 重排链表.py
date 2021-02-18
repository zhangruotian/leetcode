# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        sub_head=slow.next
        slow.next=None
        new_head=self.reverse(sub_head)
        cur1=head
        cur2=new_head
        while cur1 and cur2:
            next1=cur1.next
            next2=cur2.next
            cur1.next=cur2
            cur2.next=next1
            cur1=next1
            cur2=next2
        return head
    
    def reverse(self,head):
        prev=None
        cur=head
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev
# 快慢指针找到中点，然后后半段翻转，然后二路归并