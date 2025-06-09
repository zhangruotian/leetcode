class Solution:
    def calculate(self, s: str) -> int:
        # " 3 + 56 *56/ 56 -2 "
        prev = '+'
        i = 0 
        stack = []
        while i<len(s):
            if s[i].isdigit():
                num,new_i = self.get_num(s,i)
                if prev=='+':
                    stack.append(num)
                if prev=='-':
                    stack.append(-1*num)
                if prev=='*':
                    stack[-1] = stack[-1]*num
                if prev=='/':
                    stack[-1] = int(stack[-1]/num)
                i = new_i
                continue
            if s[i] in {'+','-','*','/'}:
                prev = s[i]
            i+=1
        return sum(stack)

    def get_num(self,s,i):
        num = 0
        while i<len(s) and s[i].isdigit():
            num = num*10+ord(s[i])-ord('0')
            i+=1
        return num,i
                

