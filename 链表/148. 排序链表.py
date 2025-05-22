# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head,_ = self.quickSort(head)
        return sorted_head
    
    def quickSort(self,head):
        if not head or not head.next: return head,head
        first_head,last_head = self.partition(head)
        first_sorted_head,first_sorted_tail = self.quickSort(first_head)
        last_sorted_head,last_sorted_tail = self.quickSort(last_head)
        if not first_sorted_tail:
            head.next = last_sorted_head
            return head, last_sorted_tail
        if not last_sorted_head:
            first_sorted_tail.next = head
            return first_sorted_head,head
        first_sorted_tail.next = head
        head.next = last_sorted_head
        return first_sorted_head,last_sorted_tail
    
    def partition(self,head):
        dummy_head_small = ListNode()
        dummy_head_large = ListNode()
        cur = head.next
        cur1,cur2 =dummy_head_small,dummy_head_large
        while cur:
            if cur.val<=head.val:
                cur1.next = cur
                cur1=cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        cur1.next = None
        cur2.next = None
        head.next = None
        return dummy_head_small.next, dummy_head_large.next
# quick sort


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
# merge sort  T:O(nlogn) S:O(logn)


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
# bottom-up T:O(nlogn) S:O(1)
