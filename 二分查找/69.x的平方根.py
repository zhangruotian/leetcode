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