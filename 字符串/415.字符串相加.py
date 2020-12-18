class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=''
        if len(num1)>len(num2):
            num2='0'*(len(num1)-len(num2))+num2
        if len(num2)>len(num1):
            num1='0'*(len(num2)-len(num1))+num1
        pointer=len(num1)-1
        add=0
        while pointer>0:
            n1=int(num1[pointer])
            n2=int(num2[pointer])
            pointer-=1
            summation=n1+n2+add
            if summation>9:
                add=1
                res+=str(summation-10)
            else:
                add=0
                res+=str(summation)
        if int(num1[0])+int(num2[0])+add>9:
            res+=(str(int(num1[0])+int(num2[0])+add-10))+'1'
        else:
            res+=str(int(num1[0])+int(num2[0])+add)

        return res[::-1]