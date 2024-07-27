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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head1, head2 = self.find_mid(head)
        new_head1 = self.sortList(head1)
        new_head2 = self.sortList(head2)
        return self.merge(new_head1,new_head2)
    
    def find_mid(self, head):
        dummy_head = ListNode()
        dummy_head.next = head
        pre, slow,fast = dummy_head, head, head
        while fast and fast.next:
            pre = pre.next
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return head, slow
    
    def merge(self, head1, head2):
        dummy_head = ListNode()
        cur = dummy_head
        cur1, cur2 = head1, head2
        while cur1 and cur2:
            if cur1.val<cur2.val:  
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2
        return dummy_head.next


# bottom-up T:O(nlogn) S:O(1)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy_head = ListNode()
        dummy_head.next = head
        step = 1
        length = self.get_len(head)
        while step<length:
            old_tail = dummy_head
            cur = dummy_head.next
            while cur:
                right = self.split(cur,step)
                if not right:
                    old_tail.next = cur
                    break
                next = self.split(right,step)
                new_head, new_tail = self.merge(cur,right)
                old_tail.next = new_head
                old_tail = new_tail
                cur = next
            step *= 2
        return dummy_head.next
    
    def merge(self, head1, head2):
        dummy_head = ListNode()
        cur1,cur2, cur = head1, head2, dummy_head
        while cur1 and cur2:
            if cur1.val<cur2.val:
                cur.next=cur1
                cur1 = cur1.next
            else:
                cur.next=cur2
                cur2 = cur2.next
            cur = cur.next
        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2
        while cur.next:
            cur=cur.next
        return dummy_head.next, cur

    # divide the linked list into two lists
    # first linked list contains n nodes
    # return the head of second linked list
    def split(self, cur, step):
        if not cur:
            return None
        for _ in range(step-1):
            if cur:
                cur =cur.next
            else:
                return cur
        if not cur:
            return None
        next = cur.next
        cur.next = None
        return next
    
    def get_len(self, head):
        l = 0
        while head:
            l+=1
            head=head.next
        return l 

