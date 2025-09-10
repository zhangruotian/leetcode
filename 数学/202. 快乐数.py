class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        slow, fast = n, self.get_next(n)
        while fast!=1:
            if slow == fast:
                return False
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        return True
    
    def get_next(self,n):
        res = 0
        for num_str in str(n):
            res+=int(num_str)**2
        return res
# https://leetcode.cn/problems/happy-number/solutions/224894/kuai-le-shu-by-leetcode-solution/
