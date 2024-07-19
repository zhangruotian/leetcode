# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA, curB = headA, headB
        while True:
            if not curA and not curB:
                return None
            if curA is curB:
                return curA
            if curA and curB:
                curA = curA.next
                curB = curB.next
            if curB and not curA:
                curA = headB
                curB = curB.next
            if curA and not curB:
                curB = headA
                curA = curA.next
# 两个指针，curA走完A走B，curB走完B走A，最后会碰到一起；或者都为none，说明无交点
# T:O(n+m) S:O(1)
