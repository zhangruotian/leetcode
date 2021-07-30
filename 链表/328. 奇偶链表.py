# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_head=head
        even_head=head.next
        odd=odd_head
        even=even_head
        cur=even_head.next
        last_odd=odd
        last_even=even
        i=3
        while cur:
            if i%2!=0:
                odd.next=cur
                odd=odd.next
                last_odd=cur
            else:
                even.next=cur
                even=even.next
                last_even=cur
            cur=cur.next
            i+=1
        last_even.next=None
        last_odd.next=even_head
        return odd_head
# 初始化odd_head和even_head往后添加即可

#头插
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev=head
        cur=head.next
        while cur and cur.next:
            next=cur.next
            cur.next=next.next
            next.next=prev.next
            prev.next=next
            prev=prev.next
            cur=cur.next
        return head