class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        x0 = x
        while True:
            diff = (x0*x0-x)/(2*x0)
            x0 = x0-diff
            if diff<1e-1:
                return math.floor(x0)

class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x+1
        while l<r:
            m = (l+r-1)//2
            if m*m == x:
                return m
            elif m*m < x:
                l = m+1
            else:
                r = m
        return l-1
