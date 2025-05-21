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
