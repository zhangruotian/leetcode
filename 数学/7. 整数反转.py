class Solution:
    def reverse(self, x: int) -> int:
        neg=False
        if x<0:
            x=-x
            neg=True
        res=0
        while x>0:
            tmp=x%10
            x=x//10
            if not neg and (res>214748364 or (res==214748364 and tmp>7)):
                return 0
            if neg and (res>214748364 or (res==214748364 and tmp>8)):
                return 0
            res=res*10+tmp
        return res if not neg else -res
#https://leetcode-cn.com/problems/reverse-integer/solution/tu-jie-7-zheng-shu-fan-zhuan-by-wang_ni_ma/