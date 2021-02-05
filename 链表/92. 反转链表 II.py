# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_node=ListNode()
        dummy_node.next=head
        prev=dummy_node
        for _ in range(m-1):
            prev=prev.next
        cur=prev.next
        for _ in range(n-m):
            next=cur.next
            cur.next=next.next
            next.next=prev.next
            prev.next=next
        return dummy_node.next
# 头插法：注意第二个for里面的顺序

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sub_prev,sub_next,sub_head,sub_tail=None,None,None,None
        dummy_head=ListNode()
        dummy_head.next=head
        prev=dummy_head
        cur=head
        for _ in range(m-1):
            prev=prev.next
        sub_prev=prev
        sub_head=prev.next
        prev=prev.next
        cur=prev.next
        for _ in range(n-m):
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        sub_tail=prev
        sub_next=cur
        sub_prev.next=sub_tail
        sub_head.next=sub_next
        return dummy_head.next
#普通方法，类似反转链表和k个一组反转链表