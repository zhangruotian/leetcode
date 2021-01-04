# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow=head
        fast=head
        count=0
        while fast:
            if count<k:
                fast=fast.next
                count+=1
            else:
                fast=fast.next
                slow=slow.next
        return slow
# T:O(n) S:O(1)