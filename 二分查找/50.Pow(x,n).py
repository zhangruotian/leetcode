class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        if n==-1:
            return 1/x
        return self.myPow(x,n//2)**2*x if n%2==1 else self.myPow(x,n//2)**2
# 递归 T:O(logn) S:O(logn)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n=abs(n)
        res=1
        while abs_n>0:
            if abs_n%2==1:
                res=res*x
            abs_n=abs_n//2
            x=x*x
        if n<0:
            return 1/res
        return res
        
# 迭代 T:O(logn) S:O(1)