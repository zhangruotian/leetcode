# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow,fast = head,head
        meet = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                meet = slow
                break
        if not meet:
            return None
        cur1,cur2 = head,meet
        while cur1!=cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
# 快慢指针
