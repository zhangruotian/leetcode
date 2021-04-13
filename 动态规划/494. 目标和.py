class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #dp[i][j]=dp[i-1][j-nums[i]]+dp[i-1][j+nums[i]]
        #dp[0][0]=1
        if sum(nums)<target:return 0
        dp=[[0]*(2*sum(nums)+1) for _ in range(len(nums)+1)]
        dp[0][0]=1
        for i in range(1,len(nums)+1):
            for j in range(-sum(nums),sum(nums)+1):
                dp[i][j]=dp[i-1][j-nums[i-1]]+dp[i-1][j+nums[i-1]]
        return dp[-1][target]

#return self.findTargetSumWays(nums[1:],target-nums[0])+neg=self.findTargetSumWays(nums[1:],target+nums[0])
#递归超时，改写为dp
#dp[i][j]=dp[i-1][j-nums[i]]+dp[i-1][j+nums[i]]
#dp[i][j]表示用前i个数计算得到j一共有多少种方法
#当nums[i]前面符号为正，dp[i][j]=dp[i-1][j-nums[i]]
#当nums[i]前面符号为负，dp[i][j]=dp[i-1][j+nums[i]]
#总共方法数为两者之和

# dp有2*sum(nums)+1列，例如[1,1,1]，j的范围为-3～3
# dp有len(nums)+1行，包括i=0
# 初始化dp[0][0]=1。
# dp与nums之间有offset,dp[i][j]=dp[i-1][j-nums[i-1]]+dp[i-1][j+nums[i-1]]
# 记得-1
