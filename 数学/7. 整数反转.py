class Solution:
    def reverse(self, x: int) -> int:
        max_ = 2**31-1
        min_ = -2**31
        if x==min_: #保证可以x=-x
            return 0
        neg = False
        if x<0:
            x = -x
            neg = True
        res = 0
        while x>0:
            if res>max_/10: #用max_就行。比如max_=14,min_=15。max_/10=1的时候对max_,min_都可以，max_/10=2的时候都不行。
                return 0
            res*=10
            if res>max_-(x%10): #用max_就行。唯一例外可能就是res+(x%10)=min_，但是-8463847412早就应该返回0了，所以用max_就行。
                return 0
            res+=(x%10)
            x=x//10
        return -res if neg else res

        
