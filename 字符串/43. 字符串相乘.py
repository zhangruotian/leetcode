class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 1 2 3         
        # 4 5 6

        # 9 9 9
        #.  9 9
        if num1[0]=='0' or num2[0]=='0':
            return '0'
        res = "0"
        for i in range(len(num2)-1,-1,-1):
            single_res = self.multi_single(num1,num2[i])+'0'*(len(num2)-1-i)
            print(single_res)
            res = self.add(res,single_res)
        return res
    
    def add(self,num1,num2):
        res = ''
        carry_over = 0
        i,j = len(num1)-1,len(num2)-1
        while i>=0 or j>=0:
            n1 = ord(num1[i])-ord('0') if i>=0 else 0
            n2 = ord(num2[j])-ord('0') if j>=0 else 0
            val = n1+n2+carry_over
            carry_over = val//10
            res = str(val%10)+res
            i-=1
            j-=1
        if carry_over:
            res = '1'+res
        return res
    
    def multi_single(self,num1, n):
        res = ''
        carry_over = 0
        n = ord(n)-ord('0')
        for i in range(len(num1)-1,-1,-1):
            n1 = ord(num1[i])-ord('0')
            val = n*n1+carry_over
            carry_over = val//10
            res = str(val%10)+res
        if carry_over:
            res = str(carry_over)+res
        return res
