# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head=ListNode()
        dummy_head.next=head
        prev,cur=dummy_head,head
        while cur and cur.next:
            if cur.val==cur.next.val:
                while cur.next and cur.val==cur.next.val:#2111(防止越界)
                    cur=cur.next
                cur=cur.next
                prev.next=cur
            else:
                cur=cur.next
                prev=prev.next
        return dummy_head.next

#注意边界条件: 1112(需要dummy_head)  2111(防止越界)