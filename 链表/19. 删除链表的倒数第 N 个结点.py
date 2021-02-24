# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #dm->1->None
        dummy_head=ListNode()
        dummy_head.next=head
        slow,fast=dummy_head,dummy_head
        for _ in range(n+1):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy_head.next
#快慢指针
#因为可能要删除第一个节点，所以需要dummy_head