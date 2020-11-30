class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        else:
            a=0
            lowest=prices[0]
            for i in range(1,len(prices)):
                a = max(a,prices[i]-lowest)
                if prices[i]<lowest:
                    lowest=prices[i]
            return a
        
# ‘最大利润’这种字眼大概率用动态规划做
# 首先找到转移方程 ：f(i)=max(选:f(i-1),不选:prices[i]-lowest)
# f(i)代表到第i天为止的最优解(最大利润)
# 与其他动态规划不同之处: 此题需要维护一个到ith天为止的最低价格lowest
# f(i)只与f(i-1)相关,无需维护装f(0),f(1)....f(n)的list。维护一个variable交替计算即可，空间复杂度O(1)
# 时间复杂度O(n)
