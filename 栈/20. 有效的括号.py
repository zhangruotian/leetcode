class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(','}':'{',']':'['}
        stack=[]
        for c in s:
            if c in d.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                pop=stack.pop()
                if d[c]!=pop:
                    return False
        return not stack
#注意三种情况false
#1. 括号匹配不上
#2. 先出现右括号
#3. stack中剩余左括号