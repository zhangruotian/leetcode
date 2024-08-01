# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur, cur1, cur2 = dummy_head, l1, l2
        carry_over = 0
        while cur1 or cur2:
            cur1_val = cur1.val if cur1 else 0
            cur2_val = cur2.val if cur2 else 0
            total = cur1_val+cur2_val+carry_over
            carry_over = total//10
            cur.next = ListNode(total%10)
            cur = cur.next
            if cur1:
                cur1=cur1.next
            if cur2:
                cur2=cur2.next
        if carry_over:
            cur.next = ListNode(1)
        return dummy_head.next
