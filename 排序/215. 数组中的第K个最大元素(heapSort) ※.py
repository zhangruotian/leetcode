# 第k大元素，维护小顶堆，只有新元素大于min_heap[0]的时候，弹出min_heap[0]，压入新元素。这样就能确定保持小顶堆中是到目前为止，最大的k的元素，且min_heap[0]是最小的(第k小)
# O(nlogk)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k,len(nums)):
            heapq.heappush(min_heap,nums[i])
            heapq.heappop(min_heap)
        return min_heap[0]
        
# 自己实现
# pushandpop只需要把min_heap[0]换成新元素，然后对index 0 往下swap就行。
# O(nlogk)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #   0
        #  1  2
        # 3 4
        # 2*i+1  2*i+2
        min_heap = nums[:k]
        self.heapify(min_heap)
        for i in range(k,len(nums)):
            if nums[i]>min_heap[0]:
                min_heap[0] = nums[i]
                self.swap_with_sons(min_heap,0)
        return min_heap[0]
    
    def heapify(self,min_heap):
        for i in range(len(min_heap)-1,-1,-1):
            self.swap_with_sons(min_heap,i)
            
    def swap_with_sons(self,min_heap,i):
        l = 2*i+1
        r = 2*i+2
        val = min_heap[i]
        if l>=len(min_heap):
            return
        elif r<len(min_heap):
            val_l = min_heap[l]
            val_r = min_heap[r]
            min_lr = l 
            if val_l>val_r:
                min_lr = r 
            if val>min_heap[min_lr]:
                min_heap[i],min_heap[min_lr] = min_heap[min_lr],min_heap[i]
                self.swap_with_sons(min_heap,min_lr)
        else:
            if val>min_heap[l]:
                min_heap[i],min_heap[l] = min_heap[l],min_heap[i]
                self.swap_with_sons(min_heap,l)
