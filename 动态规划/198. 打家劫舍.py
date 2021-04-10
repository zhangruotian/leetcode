class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        #2 7 11 11 12
        if not nums:return 0
        if len(nums)==1:return nums[0]
        a=nums[0]
        b=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            a,b=b,max(a+nums[i],b)
        return b
#dp[i]只与dp[i-1]和dp[i-2]有关，滚动累计计算即可