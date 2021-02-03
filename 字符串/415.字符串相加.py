class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 99      12
        #999     345
        i,j,res,add_one=len(num1)-1,len(num2)-1,'',0
        while i>-1 or j>-1:
            n1=ord(num1[i])-ord('0') if i>-1 else 0
            n2=ord(num2[j])-ord('0') if j>-1 else 0
            add=n1+n2+add_one
            if add>9:
                add_one=1
                res=str(add-10)+res
            else:
                add_one=0
                res=str(add)+res
            i-=1
            j-=1
        if add_one:
            res='1'+res
        return res