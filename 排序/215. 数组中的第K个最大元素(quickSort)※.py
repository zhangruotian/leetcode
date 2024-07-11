class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quickSort(nums,0,len(nums)-1)
        return nums[-k]
    
    def partition(self, nums, l ,r):
        pivot = nums[l]
        i,j = l+1, r
        while True:
            while i<=r and nums[i]<=pivot:
                i+=1
            while j>0 and nums[j]>pivot:
                j-=1
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        nums[l], nums[j] = nums[j], nums[l]
        return j
    
    def quickSort(self, nums, l,r):
        if l>=r:
            return 
        mid = self.partition(nums,l,r)
        self.quickSort(nums, l,mid-1)
        self.quickSort(nums,mid+1,r)
# quicksort (best nlogn, worst n^2)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        l,r,target = 0,length-1, length-k
        return self.findKthLargestRecur(nums,l,r,target)
    
    def partition(self, nums, l, r):
        pivot = nums[l]
        i, j = l+1, r
        while True:
            while i<=r and nums[i]<=pivot:
                i+=1
            while j>0 and nums[j]>pivot:
                j-=1
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        nums[j], nums[l] = nums[l], nums[j]
        return j
    
    def findKthLargestRecur(self, nums, l, r, target):
        mid = self.partition(nums,l,r)
        if mid == target:
            return nums[mid]
        if mid < target:
            return self.findKthLargestRecur(nums,mid+1,r,target)
        if mid > target:
            return self.findKthLargestRecur(nums,l,mid-1,target)
# partition找到那个k的位置就行，无需全部sort
# leetcode加了case，已经过不去了
