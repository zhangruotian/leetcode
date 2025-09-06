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
'''
解释一下为什么外层要对coins循环：

假设coins = {1, 2, 3}，amount = 5。 凑出5的方案有三类：

组合必须以硬币1结尾，且不能包含硬币1之后的其他硬币2， 3。假设这类方案数量为x1。
组合必须以硬币2结尾，且不能包含硬币2之后的其他硬币3。假设这类方案数量为x2。
组合必须以硬币3结尾。假设这类方案数量为x3。
第一轮，我们计算x1。
第二轮，我们计算x2。并将x2加到x1上，得到x1 + x2。
第三轮，我们计算x3。并将x2加到x1 + x2上，得到x1 + x2 + x2。

对amount为5而言
x1 有 {1, 1, 1, 1, 1}
x2 有 {1, 1, 1, 2},  {1, 2, 2}
x3 有 {1, 1, 3}, {2, 3}
最终返回x1 + x2 + x2。
'''
