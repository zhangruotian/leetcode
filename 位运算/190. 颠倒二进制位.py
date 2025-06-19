class Solution:
    def reverseBits(self, n: int) -> int:
        # 101101
        res = 0
        for _ in range(32):
            res = (res<<1) | (n&1) 
            n = n>>1
        return res
