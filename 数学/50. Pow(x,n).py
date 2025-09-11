class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        if n>0:
            return self.myPowPosN(x,n)
        return 1/self.myPowPosN(x,-n)

    def myPowPosN(self,x,n):
        if n==1:
            return x
        half_n = self.myPow(x,n//2)
        if n%2==0:
            return half_n*half_n
        else:
            return half_n*half_n*x
