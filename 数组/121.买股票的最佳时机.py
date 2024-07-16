class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(prices[i]-lowest, max_profit)
            lowest = min(lowest,prices[i])
        return max_profit
# 买的那天一定是卖的那天之前的最小值。 每到一天，维护那天之前的最小值即可。
