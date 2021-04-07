class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax=nums[0]
        fmin=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            temp=fmax #fmin应该用fmax更新前的值
            fmax=max(nums[i],fmax*nums[i],fmin*nums[i])
            fmin=min(nums[i],temp*nums[i],fmin*nums[i])
            if fmax>res:
                res=fmax
        return res
# 动态规划
# 基本思路：一个fmax，记录以ith为结尾的子数组的最大值
#         fmax=max(nums[i],fmax*nums[i],fmin*nums[i])
#         一个fmin，记录以ith为结尾的子数组的最小值
#。       fmin=min(nums[i],temp*nums[i],fmin*nums[i])
#         res记录最大值，返回
# S:O(1) T:O(n)