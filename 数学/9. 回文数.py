class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False  
        if x//10!=0 and x%10==0:return False #各位为0，且是两位数或两位以上(019)
        left=x
        right=0
        i=0
        while True:
            if left==right:
                return True
            if left<right and left==right//10:
                return True
            if left<right and left!=right//10:
                return False
            num=x//(10**i)%10
            left=x//(10**(i+1))
            right=right*10+num
            i+=1

#1234
#拿10位: 1234//10=123 123%10=3
#拿100位  1234//100=12 12%10=2
#拿i位:  n//(10**i)%10