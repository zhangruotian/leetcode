class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n==1: return 0
        return self.lastRemaining(n-1,m)+m%n
# 约瑟夫环