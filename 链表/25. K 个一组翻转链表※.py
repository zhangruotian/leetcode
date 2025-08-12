# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        prev_tail = dummy_head
        old_head = head
        while True:
            ifreverse = self.ifreverse(old_head,k)
            if ifreverse:
                new_head,new_tail,old_head = self.reverse(old_head,k)
                prev_tail.next = new_head
                prev_tail = new_tail
            else:
                prev_tail.next = old_head
                break
        return dummy_head.next
    
    def ifreverse(self,old_head,k):
        cur = old_head
        for _ in range(k):
            if not cur:
                return False
            cur=cur.next
        return True
    
    def reverse(self,old_head,k):
        prev = None
        cur = old_head
        for _ in range(k):
            next = cur.next
            cur.next = prev
            prev = cur 
            cur=next
        return prev,old_head,cur
