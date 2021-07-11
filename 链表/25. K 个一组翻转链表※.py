# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 模拟
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
# sh        st       
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
#cur
# tail=dummy_node
# new_head,new_tail=reverse(sh,st)
# count

#头插法
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head=ListNode()
        dummy_head.next=head
        prev=dummy_head
        cur=head
        while True:
            if self.greaterOrEqualThanK(prev,k):
                prev,cur=self.helper(prev,cur,k-1)
            else:
                return dummy_head.next

    def helper(self,prev,cur,t):
        # 头插
        for _ in range(t):
            next=cur.next
            cur.next=next.next
            next.next=prev.next
            prev.next=next
        prev=cur
        cur=cur.next
        return prev,cur
    
    def greaterOrEqualThanK(self,prev,k):
        #判断是否还需要反转
        prev=prev.next
        for _ in range(k):
            if not prev:return False
            prev=prev.next
        return True

# 改编题：不足k也翻转
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head=ListNode()
        dummy_head.next=head
        prev=dummy_head
        cur=head
        while True:
            prev,cur=self.helper(prev,cur,k)
            if not cur:
                return dummy_head.next
    
    def helper(self,prev,cur,k):
        for _ in range(k-1):
            next=cur.next
            if not next:
                return None,None
            cur.next=next.next
            next.next=prev.next
            prev.next=next
        
        return cur,cur.next
        
        












