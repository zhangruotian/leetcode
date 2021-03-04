class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        #dp[0]=nums[0]
        #dp[1]=max(nums[1],nums[0])
        if not nums:return 0
        if len(nums)==1:return nums[0]
        n=len(nums)
        a=nums[0]
        b=max(nums[0],nums[1])
        for i in range(2,n):
            c=max(b,a+nums[i])
            a=b
            b=c
        return b
#dp[i]只与dp[i-1]和dp[i-2]有关，滚动累计计算即可