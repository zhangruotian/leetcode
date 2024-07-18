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
# 暴力算法T:O(nkk)
# 用heap把k->logk

#手动heapify和pop
#如果堆顶的node有next，则lists[0]=node.next   heapify(lists,0,l)
#如果堆顶的node无next，则交换头尾node，把尾pop。 heapify(lists,0,l-1)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists=[node for node in lists if node]
        l=len(lists)
        for i in range(l//2-1,-1,-1):
            self.heapify(lists,i,l)
        dummy_head=ListNode()
        cur=dummy_head
        while lists:
            top=lists[0]
            cur.next=top
            cur=cur.next
            next=top.next
            if next:
                lists[0]=next
                self.heapify(lists,0,l)
            else:
                lists[0],lists[l-1]=lists[l-1],lists[0]
                lists.pop()
                if not lists:
                    break
                l-=1
                self.heapify(lists,0,l)
        return dummy_head.next

    def heapify(self,lists,i,l):
        left=2*i+1
        right=2*i+2
        min_index=i 
        if left<l and lists[min_index].val>lists[left].val:
            min_index=left
        if right<l and lists[min_index].val>lists[right].val:
            min_index=right
        lists[min_index],lists[i]=lists[i],lists[min_index]
        if i!=min_index:
            self.heapify(lists,min_index,l)

#两两merge。类似merge sort O(nklog(k))
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        while len(lists)>1:
            new_lists = []
            for i in range(0,len(lists),2):
                cur = lists[i]
                if i+1<len(lists):
                    next = lists[i+1]
                    new_head=self.merge(cur,next)
                    new_lists.append(new_head)
                else:
                    new_lists.append(cur)
            lists = new_lists
        return lists[0] 
     
    def merge(self,cur,next):
        dummy_head = ListNode()
        i = dummy_head
        while cur and next:
            if cur.val<= next.val:
                i.next = cur
                cur = cur.next
            else:
                i.next = next
                next=next.next
            i = i.next
        if cur:
            i.next = cur
        if next:
            i.next = next
        return dummy_head.next
        
        
