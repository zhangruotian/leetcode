class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float(inf)]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):  #实现方式
            for coin in coins:
                if i-coin>=0:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return -1 if dp[-1]==float(inf) else dp[-1]

#dp[i]=min(dp[i-1],dp[i-2],dp[i-3])+1
#实现方式
#i-coin<0的跳过