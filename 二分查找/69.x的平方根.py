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
    def mySqrt(self, x: int,precision: int) -> int:
        if x==0: return 0
        r1,r2,x=float(x),float(x),float(x)
        while True:
            r2=0.5*(r1+x/r1)
            if abs(r2-r1)<1e-31:
                return round(r2,precision)
            r1=r2