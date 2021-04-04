# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow if not fast else slow.next