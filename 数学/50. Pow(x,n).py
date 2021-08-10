class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.pow(x,n) if n>=0 else 1.0/self.pow(x,-n)

    def pow(self,x,n):
        if n==0:
            return 1
        y=self.pow(x,n//2)
        return y*y if n%2==0 else y*y*x  
        # y**2报错：numerical values overflow
# 递归 T:O(logn) S:O(logn)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n=abs(n)
        res=1
        while abs_n>0:
            if abs_n&1:
                res*=x
            x=x*x
            abs_n>>=1
        return res if n>=0 else 1/res
        
# 迭代 T:O(logn) S:O(1)
#快速幂 笔记