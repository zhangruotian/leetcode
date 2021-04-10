class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        if len(nums)==1:return nums[0]

        a,b=nums[0],nums[0]
        for i in range(2,len(nums)-1):
            a,b=b,max(a+nums[i],b)
        res1=b

        a,b=0,nums[1]
        for i in range(2,len(nums)):
            a,b=b,max(a+nums[i],b)
        res2=b
        return max(res1,res2)
#分两种情况：1.选第1个，则最后一个不能选
# 2.不选第1个，则最后一个可选
# max(1,2)

class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        if len(nums)==1:return nums[0] 
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        if len(nums)==1:return nums[0]
        a,b=nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            a,b=b,max(a+nums[i],b)
        return b
# max(rob(nums[1:]),rob(nums[:-1]))