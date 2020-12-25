# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        sub_head=head
        sub_tail=head
        cur=head
        count=0
        tail=ListNode(0)
        tail.next=head
        res=tail
        while cur:
            count += 1
            if count % k == 0:
                sub_tail = cur
                cur=cur.next
                new_head, new_tail = self.reverse(sub_head, sub_tail)
                tail.next = new_head
                tail = new_tail
                sub_head = cur
            else:
                cur=cur.next
        tail.next = sub_head
        return res.next
                
    def reverse(self,head,tail):
        tail.next=None
        pre=None
        cur=head
        while cur.next:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        cur.next=pre
        return cur,head