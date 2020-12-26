# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_node=ListNode(0)
        tail=dummy_node
        sub_head,sub_tail=head,0
        counter=1
        cur=head
        while cur:
            if counter%k==0:
                next=cur.next
                counter+=1
                sub_tail=cur
                new_head,new_tail=self.reverse(sub_head,sub_tail)
                tail.next=new_head
                tail=new_tail
                sub_head=next
                cur=next
            else:                  # 注意此处应该是if else的关系
                counter+=1
                cur=cur.next

        tail.next=sub_head
        return dummy_node.next

    def reverse(self,sub_head,sub_tail):
        sub_tail.next=None
        pre=None
        cur=sub_head
        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        return pre,sub_head
        
