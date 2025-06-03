class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minium,maxinum = nums[0],nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            new_minimum = min(minium*num,maxinum*num,num)
            new_maxinum = max(minium*num,maxinum*num,num)
            res = max(res,new_maxinum)
            minium,maxinum = new_minimum,new_maxinum
        return res
# 动态规划
# 基本思路：一个fmax，记录以ith为结尾的子数组的最大值
#         fmax=max(nums[i],fmax*nums[i],fmin*nums[i])
#         一个fmin，记录以ith为结尾的子数组的最小值
#。       fmin=min(nums[i],temp*nums[i],fmin*nums[i])
#         res记录最大值，返回
# S:O(1) T:O(n)
