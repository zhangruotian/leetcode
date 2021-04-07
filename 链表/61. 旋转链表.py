# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:return
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        k=k%n
        if k==0:return head

        newhead,newtail=self.reverse(head)
        cur=newhead
        for i in range(k-1):
            cur=cur.next
        next=cur.next
        cur.next=None
        head1,tail1=self.reverse(newhead)
        head2,tail2=self.reverse(next)
        tail1.next=head2
        return head1

    def reverse(self,head):
        prev=None
        cur=head
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev,head
#跟189旋转数组一样，先整体旋转，再旋转前后两个部分
#需扫描链表三次

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:return
        dummy_head=ListNode()
        dummy_head.next=head
        prev,cur,n=dummy_head,head,0
        while cur:
            n+=1
            cur=cur.next
            prev=prev.next
        prev.next=head

        k=k%n
        cur=head
        for _ in range(n-k-1):
            cur=cur.next
        next=cur.next
        cur.next=None
        return next
#将链表成环，然后在n-k-1的位置断开，返回next
#扫描2趟
#https://leetcode-cn.com/problems/rotate-list/solution/huan-zhuang-lian-biao-yi-dong-pei-tu-by-e4ybr/