# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        new_head=self.inPlaceReverse(slow)
        while new_head:
            if new_head.val !=head.val:
                return False
            new_head=new_head.next
            head=head.next
        return True

    def inPlaceReverse(self,head):
        pre=None
        cur=head
        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        return pre
     
# 快慢指针找中点，inplace反转后面链表。判断与前半部分是否一样。
# T:O(n) S:O(1)
 
        





