class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        res1,res2=0,0
        a,b = 0,nums[1]
        for i in range(2,len(nums)):
            a,b=b,max(b,a+nums[i])
        res1 = b

        a,b = 0,nums[0]
        for i in range(1,len(nums)-1):
            a,b=b,max(b,a+nums[i])
        res2 = b
        return max(res1,res2)

# 由于房屋是环形排列，第一家和最后一家是相邻的，所以它们 不能同时被抢。

# 因此，最大金额的抢劫方案必然出自以下两种情况之一：
# 不抢第一家：这样我们就可以在从第二家到最后一家的范围内（即数组 nums[1:]）进行标准的“打家劫舍”。
# 不抢最后一家：这样我们就可以在从第一家到倒数第二家的范围内（即数组 nums[:-1]）进行标准的“打家劫舍”。
