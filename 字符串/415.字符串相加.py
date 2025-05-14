class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j = len(num1)-1,len(num2)-1
        carry = 0
        res = ''
        while i>=0 or j>=0:
            numi = ord(num1[i])-ord('0') if i>=0 else 0
            numj = ord(num2[j])-ord('0') if j>=0 else 0
            sum_ij = numi+numj+carry
            res_ij = str(sum_ij%10)
            carry = sum_ij//10
            res = res_ij+res
            i-=1
            j-=1
        return res if carry==0 else '1'+res
