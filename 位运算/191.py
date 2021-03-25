class Solution:
    def hammingWeight(self, n: int) -> int:
        # res=0
        # for i in range(32):
        #     if n & (1<<i):
        #         res+=1
        # return res

        res=0
        while n:
            n=n&(n-1)
            res+=1
        return res
#https://leetcode-cn.com/problems/number-of-1-bits/solution/wei-1de-ge-shu-by-leetcode-solution-jnwf/