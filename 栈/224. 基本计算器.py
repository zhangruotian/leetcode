class Solution:
    def calculate(self, s: str) -> int:
        stack=[1]
        pre_sign=1
        num=0
        res=0
        for i,c in enumerate(s):
            if c==" " and i!=len(s)-1:continue
            if c.isdigit():
                num=num*10+(ord(c)-ord("0"))
            if not c.isdigit() or i==len(s)-1:
                res+=num*pre_sign
                num=0
                if c=="+":
                    pre_sign=stack[-1]
                elif c=='-':
                    pre_sign=-1*stack[-1]
                elif c=="(":
                    stack.append(pre_sign)
                elif c==")":
                    stack.pop()
        return res
