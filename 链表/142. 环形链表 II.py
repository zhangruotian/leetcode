# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return 
        slow=head
        fast=head
        s1=head
        s2=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow is fast:
                if slow==head:
                    return head
                s2=slow
                break
        if not s2:
            return 
        while True:
            s1=s1.next
            s2=s2.next
            if s1 is s2:
                return s1
# 快慢指针
