class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                res+=prices[i]-prices[i-1]
        return res
#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/best-time-to-buy-and-sell-stock-ii-zhuan-hua-fa-ji/