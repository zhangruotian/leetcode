class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        if nums[pivot]<=target<=nums[-1]:
            return self.binary_search(nums,target,pivot,len(nums))
        else:
            return self.binary_search(nums, target, 0, pivot)

    def find_pivot(self, nums):
        l,r = 0, len(nums)
        while l<r:
            m = (l+r-1)//2
            if nums[m] > nums[-1]:
                l = m+1
            if nums[m] < nums[-1]:
                r = m
            if nums[m] == nums[-1]:
                return m
        return l 

    def binary_search(self,nums, target, l, r):
        while l<r:
            m = (l+r-1)//2
            if nums[m] < target:
                l = m+1
            if nums[m] > target:
                r = m
            if nums[m] == target:
                return m
        return -1
        
# 先找到最小值索引，然后就可二分查找


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)
        while l<r:
            m=(l+r-1)//2
            if target==nums[m]:
                return m
            else:
                if nums[m]>nums[len(nums)-1]:
                    if target>=nums[0] and target<nums[m]:
                        r=m
                    else:
                        l=m+1
                else:
                    if target>nums[m] and target<=nums[len(nums)-1]:
                        l=m+1
                    else:
                        r=m
        return -1
# 可直接判断，代码更短，速度更快
