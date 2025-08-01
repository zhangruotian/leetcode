#单调队列 O(n)
#https://www.youtube.com/watch?v=2SXqBsTR6a8
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for i in range(len(nums)):
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            if i-q[0]==k:
                q.popleft()
            if i>=k-1:
                res.append(nums[q[0]])
        return res


# heap O(nlogk)
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        for i in range(k):
            max_heap.append((-nums[i],i))

        heapq.heapify(max_heap)
        res.append(-max_heap[0][0])
        for i in range(k,len(nums)):
            heapq.heappush(max_heap,(-nums[i],i))
            while max_heap[0][1]<=i-k:
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])
        return res
        
