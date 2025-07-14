class Solution:
    def calculate(self, s: str) -> int:
        # " -3+26 *23 /21 +2 "
        s = s+'+'
        stack = [0]
        prev_op = '+'
        for c in s:
            if c==' ': continue
            if not c.isdigit():
                if prev_op=='-':
                    stack[-1] = -1*stack[-1]
                if prev_op=='*':
                    stack[-2] = stack[-2]*stack[-1]
                    stack.pop()
                if prev_op=='/':
                    stack[-2] = int(stack[-2]/stack[-1])
                    stack.pop()
                stack.append(0)
                prev_op = c
            else:
                stack[-1] = stack[-1]*10+int(c)
        return sum(stack)
        
                




        
