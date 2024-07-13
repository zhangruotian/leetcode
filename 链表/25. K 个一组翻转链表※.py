# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        last_tail = dummy_node
        new_head = head
        while self.need_reverse(new_head,k):
            last_tail, new_head = self.reverse(last_tail,new_head,k)
        last_tail.next = new_head
        return dummy_node.next

    
    def need_reverse(self,new_head,k):
        num_left = 0
        cur = new_head
        while cur:
            num_left+=1
            cur = cur.next
        return True if num_left>=k else False


    def reverse(self, last_tail, new_head,k):
        prev = new_head
        cur = new_head.next
        for _ in range(k-1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        last_tail.next = prev
        return new_head,cur
        
