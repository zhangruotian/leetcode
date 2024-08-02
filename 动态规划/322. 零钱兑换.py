class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 2 5  10 dp[1]=-1 dp[2]=1 dp[3]
        # 2 3
        dp = [0]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            min_num = float('inf')
            for coin in coins:
                if i-coin<0 or dp[i-coin]==-1:
                    continue
                else:
                    min_num = min(dp[i-coin],min_num)
            if min_num==float('inf'):
                dp[i] = -1
            else:
                dp[i] = min_num+1
        return dp[-1]

#dp[i]=min(dp[i-1],dp[i-2],dp[i-3])+1

#实现方式
#i-coin<0的跳过，dp[i-coin]==-1的跳过
#如果没找到能接上的，dp[i]=-1，如果接上了，dp[i] = min+1
