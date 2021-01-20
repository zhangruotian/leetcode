# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1=l1
        cur2=l2
        head=ListNode(0)
        cur=head
        while True:
            if cur1 and cur2:
                sum_val=cur.val+cur1.val+cur2.val
                cur1=cur1.next
                cur2=cur2.next
            elif cur1:
                sum_val=cur1.val+cur.val
                cur1=cur1.next
            elif cur2:
                sum_val=cur2.val+cur.val
                cur2=cur2.next
            else:
                break
            
            if sum_val>=10:
                cur.val=sum_val-10
                cur.next=ListNode(1)
            else:
                cur.val=sum_val
                cur.next=ListNode(0)
            
            prev=cur
            cur=cur.next
        
        if  cur.val==0:
            prev.next=None
            
        return head