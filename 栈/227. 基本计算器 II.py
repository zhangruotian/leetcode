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

# new code
class Solution:
class Solution:
    def calculate(self, s: str) -> int:
        # 312+21*2 - 31/2+1
        stack = []
        i = 0
        prev = "+"
        while i<len(s):
            if s[i].isdigit():
                i,num = self.get_num(s,i)
                if prev=="+":
                    stack.append(num)
                elif prev=="-":
                    stack.append(-num)
                elif prev=="*":
                    stack[-1] = stack[-1]*num
                elif prev=="/":
                    stack[-1] = int(stack[-1]/num)
            if i==len(s):
                break
            if s[i] in {"+","-","*","/"}:
                prev = s[i]
            i+=1
        return sum(stack)

    def get_num(self,s,i):
        num = 0
        while i<len(s) and s[i].isdigit():
            num = num*10+ord(s[i])-ord('0')
            i+=1
        return i,num


