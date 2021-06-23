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


# 猴子补丁
# 几个方法： list=[] heapq.heappush(list,node) list为空，一个个添加 nlog(n)
# popped_node=heapq.heappop(list)
# heapq.heapify(list) list为初始列表，直接原地heapify  O(n)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or lists==[None]*len(lists): return None
        def __lt__(self,other):
            return self.val<other.val
        ListNode.__lt__=__lt__

        import heapq
        heap=[]
        for node in lists:
            if node:
                heapq.heappush(heap,node)
        dummy_head=ListNode()
        cur=dummy_head

        while heap:
            popped=heapq.heappop(heap)
            next=popped.next
            popped.next=None
            cur.next=popped
            cur=cur.next
            if next:
                heapq.heappush(heap,next)
        return dummy_head.next
        
        
