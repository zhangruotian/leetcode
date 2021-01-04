# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy_head=ListNode(0)
        cur=dummy_head
        head=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head,(lists[i].val,i))
                lists[i]=lists[i].next
        while head:
            min_val,min_index=heapq.heappop(head)
            if lists[min_index]:
                heapq.heappush(head,(lists[min_index].val,min_index))
                lists[min_index]=lists[min_index].next
            cur.next=ListNode(min_val)
            cur=cur.next
        return dummy_head.next
# k组，每组n个。T:O(nklogk) 
# 暴力算法T:O(nkk)
# 用heap把k->logk