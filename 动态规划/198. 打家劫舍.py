class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b = 0,nums[0]
        for i in range(1,len(nums)):
            a,b = b,max(b,a+nums[i])
        return b
#dp[i]=max(dp[i-2]+nums[i],dp[i-1])
#dp[i]只与dp[i-1]和dp[i-2]有关，滚动累计计算即可
