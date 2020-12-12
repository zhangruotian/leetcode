class Solution:
    def searchInsert(self, nums,target) :
        l=0
        r=len(nums)
        res=len(nums)
        while l<r:
            m=(l+r-1)//2
            if nums[m]==target:
                return m
            if nums[m]>target:
                res=m
                r=m
            if nums[m]<target:
                l=m+1
        return res
        
# 二分查找模板稍微修改
