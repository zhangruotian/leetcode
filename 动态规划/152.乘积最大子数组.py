class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax=nums[0]
        fmin=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            temp=fmax
            fmax=max(nums[i],fmax*nums[i],fmin*nums[i])
            fmin=min(nums[i],temp*nums[i],fmin*nums[i])
            if fmax>res:
                res=fmax
        return res
# 动态规划
# S:O(1)