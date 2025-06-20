class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            if n&1:
                res+=1
            n = n>>1
        return res
