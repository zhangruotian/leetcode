class Solution:
    def mySqrt(self, x: int) -> int:
        l,r,res=0,x+1,-1
        while l<r:
            m=(l+r-1)//2
            if m**2==x:
                return m
            elif m**2<x:
                res=m
                l=m+1
            else:
                r=m
        return res
        
# 从[0,x]范围内二分查找

# 牛顿法，可满足精度要求
class Solution:
    import math
    def mySqrt(self, x: int) -> int:
        if x ==0 or x ==1:
            return x
        return math.floor(self.mySqrtPrec(x,1e-7))
        
    def mySqrtPrec(self, x, precision):
        r1,r2 = float(x),float(x)
        while True:
            r2 = 0.5*(r1+x/r1)
            if abs(r2-r1)<precision and abs(r2*r2-x)<precision:
                return r2
            r1 = r2
