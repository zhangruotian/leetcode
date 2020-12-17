class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=self.find_pivot(nums)
        if nums[start]<=target<=nums[len(nums)-1]:
            return self.binarySearch(nums,target,start,len(nums))
        else:
            return self.binarySearch(nums,target,0,start)

    def find_pivot(self, nums):
        if len(nums)==1:
            return 0
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r - 1) // 2
            if nums[m] > nums[r-1]:
                l = m + 1
            elif nums[m] < nums[r-1]:
                r = m+1
            else:
                return l

    def binarySearch(self,nums,target,l,r):
        while l<r:
            m=(l+r-1)//2
            if nums[m]==target:
                return m
            if nums[m]>target:
                r=m
            else:
                l=m+1
        return -1
        
# 先找到最小值索引，然后就可二分查找