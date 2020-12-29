# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        curA=headA
        curB=headB
        while True:
            if curA is curB:
                return curA
            elif not curA.next and not curB.next:
                return None
            elif not curA.next:
                curA=headB
                curB=curB.next
            elif not curB.next:
                curB=headA
                curA=curA.next
            else:
                curA=curA.next
                curB=curB.next
# 两个指针，走完A走B，最后会碰到一起
# T:O(n+m) S:O(1)