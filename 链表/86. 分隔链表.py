# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_small=ListNode()
        dummy_large=ListNode()
        cur_small,cur_large=dummy_small,dummy_large
        cur=head
        while cur:
            print(cur.val)
            if cur.val<x:
                cur_small.next=cur
                cur_small=cur_small.next
            else:
                cur_large.next=cur
                cur_large=cur_large.next
            cur=cur.next
        cur_small.next=dummy_large.next
        cur_large.next=None
        return dummy_small.next
# 初始化大，小链表，最后拼接。记得把大链表最后指向none

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_head=ListNode()
        dummy_head.next=head
        left=dummy_head
        prev,cur=dummy_head,head
        while cur:
            if cur.val<x:
                next=cur.next
                prev.next=next
                cur.next=left.next
                left.next=cur
                left=cur
                cur=next
                if prev.next!=cur:
                    prev=prev.next
            else:
                cur=cur.next
                prev=prev.next
        return dummy_head.next

#原链表修改。

