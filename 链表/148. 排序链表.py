# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#quickSort超时
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.quickSort(head,None)

    def partition(self,start,end):
        head,tail=start,start
        cur=start.next
        while cur is not end:
            next=cur.next
            if cur.val<start.val:
                cur.next=head
                head=cur
            else:
                tail.next=cur
                tail=cur
            cur=next
        tail.next=end
        return head,start

    def quickSort(self,start,end):
        if start is end:
            return start
        s,m=self.partition(start,end)
        head=self.quickSort(s,m)
        m.next=self.quickSort(m.next,end)
        return head

# merge sort  T:O(nlogn) S:O(logn)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.mergeSort(head)

    def merge(self,head1,head2):
        cur1=head1
        cur2=head2
        dummy_head=ListNode()
        cur=dummy_head
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next=cur1
                cur1=cur1.next
            else:
                cur.next=cur2
                cur2=cur2.next
            cur=cur.next
        cur.next=cur1 or cur2
        return dummy_head.next

    def midCut(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        new_head=slow.next
        slow.next=None
        return head,new_head

    def mergeSort(self,head):
        if not head or not head.next:
            return head
        head1,head2=self.midCut(head)
        new_head1=self.mergeSort(head1)
        new_head2=self.mergeSort(head2)
        return self.merge(new_head1,new_head2)


# bottom-up T:O(nlogn) S:O(1)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        length=0
        cur=head
        while cur:
            cur=cur.next
            length+=1
        step=1
        dummy_head=ListNode()
        dummy_head.next=head
        while step<length:
            cur=dummy_head.next
            tail=dummy_head
            while cur:
                left=cur
                right=self.split(cur,step)
                cur=self.split(right,step)
                tail=self.merge(left,right,tail)
            step*=2
        return dummy_head.next
        
    # merge 2 sorted lists, and append the result to head
    # return the tail
    def merge(self,head1,head2,tail):
        cur1=head1
        cur2=head2
        dummy_head=ListNode()
        cur=dummy_head
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next=cur1
                cur1=cur1.next
            else:
                cur.next=cur2
                cur2=cur2.next
            cur=cur.next
        cur.next=cur1 or cur2
        while cur.next: cur=cur.next
        tail.next=dummy_head.next
        return cur

    # divide the linked list into two lists
    # first linked list contains n nodes
    # return the head of second linked list
    def split(self,head,n):
        for _ in range(n-1):
            if head:
                head=head.next
            else:
                break
        if not head:
            return None
        second=head.next
        head.next=None
        return second
