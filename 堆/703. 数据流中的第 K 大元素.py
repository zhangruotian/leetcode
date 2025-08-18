import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap)>k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
# 第k大元素，维护小顶堆，只有新元素大于min_heap[0]的时候，弹出min_heap[0]，压入新元素。这样就能确定保持小顶堆中是到目前为止，最大的k的元素，且min_heap[0]是最小的(第k小)
# O(nlogk)
