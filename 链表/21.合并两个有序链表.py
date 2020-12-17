# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead=ListNode(-1)
        cur =prehead
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next=ListNode(l1.val)
                l1=l1.next
            else:
                cur.next=ListNode(l2.val)
                l2=l2.next
            cur=cur.next
        if not l1:
            cur.next=l2
        if not l2:
            cur.next=l1
        return prehead.next