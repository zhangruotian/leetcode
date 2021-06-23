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

# recursion
# list1[0]+merge(list1[1:],list2)  if list1[0]<list2[0]
# list2[0]+merge(list1,list2[1:])  otherwise
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val<=l2.val:
            merged=self.mergeTwoLists(l1.next,l2)
            l1.next=merged
            return l1
        else:
            merged=self.mergeTwoLists(l1,l2.next)
            l2.next=merged
            return l2
