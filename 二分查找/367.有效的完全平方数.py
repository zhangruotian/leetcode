class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r=num+1
        while l<r:
            m=(l+r-1)//2
            if m**2==num:
                return True
            elif m**2>num:
                r=m
            else:
                l=m+1
        return False