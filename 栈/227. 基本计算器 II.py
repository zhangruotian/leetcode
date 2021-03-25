class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        pre_sign="+"
        for i,c in enumerate(s):
            if c==" " and i!=len(s)-1:continue
            if c.isdigit():
                num=num*10+(ord(c)-ord("0"))
            if (not c.isdigit()) or i==len(s)-1:
                if pre_sign=="+":
                    stack.append(num)
                elif pre_sign=="-":
                    stack.append(-num)
                elif pre_sign=="*":
                    stack.append(stack.pop()*num)
                elif pre_sign=="/":
                    stack.append(int(stack.pop()/num))
                num=0
                pre_sign=c
        return sum(stack)

#https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-by-leetcode-solutio-cm28/

