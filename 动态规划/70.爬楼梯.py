class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        a,b=1,2
        for _ in range(n-2):
            a,b=b,a+b
        return b
# 动态规划
# T:O(n) S:O(1) 不需要记录所有的f(i)，只需要最后的f(n)，因此交替计算即可
