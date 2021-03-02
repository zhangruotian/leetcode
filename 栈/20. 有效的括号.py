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