class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heapSort(nums)
        return nums[-k]
        
    def heapSort(self,nums):
        l=len(nums)
        for i in range(l//2-1,-1,-1):
            self.heapify(i,l,nums)
        for j in range(l-1,-1,-1):
            nums[0],nums[j]=nums[j],nums[0]
            self.heapify(0,j,nums)
        
    def heapify(self,i,l,nums):
        left=i*2+1
        right=i*2+2
        max_index=i
        if left<l and nums[left]>nums[i]:
            max_index=left
        if right<l and nums[right]>nums[max_index]:
            max_index=right
        if max_index!=i:
            nums[max_index],nums[i]=nums[i],nums[max_index]
            self.heapify(max_index,l,nums)
# 堆排序实现 https://zhuanlan.zhihu.com/p/105624690
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/shu-zu-zhong-de-di-kge-zui-da-yuan-su-by-leetcode-/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq._heapify_max(nums)
        for _ in range(k):
            res=heapq._heappop_max(nums)
        return res
# python自带堆排序(heapify 小顶堆 _heapify_max 大顶堆)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=len(nums)
        self.buildHeap(nums,l)
        for j in range(l-1,l-1-k,-1):
            nums[0],nums[j]=nums[j],nums[0]
            self.heapify(0,j,nums)
        return nums[-k]
    
    def buildHeap(self,nums,l):
        for i in range(l//2-1,-1,-1):
            self.heapify(i,l,nums)
        
    def heapify(self,i,l,nums):
        left=i*2+1
        right=i*2+2
        max_index=i
        if left<l and nums[left]>nums[i]:
            max_index=left
        if right<l and nums[right]>nums[max_index]:
            max_index=right
        if max_index!=i:
            nums[max_index],nums[i]=nums[i],nums[max_index]
            self.heapify(max_index,l,nums)
#改进版，因为只需第k大，所以heap中大的数往后放时只需放k次，无需把整个nums都排序。
#时间复杂度：O(nlogn)，建堆的时间代价是 O(n)，删除的总代价是O(klogn)，因为 k < n，故渐进时间复杂为 O(n+klogn)=O(nlogn)。



