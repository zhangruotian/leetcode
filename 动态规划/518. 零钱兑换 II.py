class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[i][j] 用前i个硬币组成amount j的组合数
        #dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]  若第i个只用一次，则dp[i-1][j-coins[i]]。前面写的代表可用无数次。
        #dp[0][j]=0
        #dp[i][0]=1
        #dp[0][0]=1
        dp=[[0]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(amount+1):
            dp[0][i]=0
        for i in range(len(coins)+1):
            dp[i][0]=1
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if j-coins[i-1]<0:    #直接跳过
                    dp[i][j]=dp[i-1][j]  #i-1 防止越界
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
        return dp[-1][-1]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[i] amount为i时的方法数
        #dp[i]=dp[i-1]+dp[i-2]+dp[i-5]
        #dp[i]+=dp[i-coins[j]]
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for i in range(1,amount+1):
                if i-coin>=0:
                    dp[i]+=dp[i-coin]
        return dp[-1]
#与爬楼梯一样的转移方程，但本题不允许重复。1 2与2 1是同一种情况。
#要重复则for i在外面。不要，则for coin在外面