class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')','[':']','{':'}'}
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack or pairs[stack.pop()]!=c:
                    return False
        return False if stack else True
# 利用栈来匹配后面的符号    
        
   
