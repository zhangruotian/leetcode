class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # rest[i] = max(rest[i-1],sold[i-1])
        # hold[i] = max(hold[i-1],rest[i-1]-prices[i])
        # sold[i] = hold[i-1]+price[i]
        rest,hold,sold = 0,-prices[0],0
        for i in range(1,len(prices)):
            rest,hold,sold = max(rest,sold),max(hold,rest-prices[i]),hold+prices[i]
        return max(rest,hold,sold)

# https://www.youtube.com/watch?v=oL6mRyTn56M
