class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        lookup={'(':')','{':'}','[':']'}
        for parenthesis in s:
            if parenthesis in lookup:
                stack.append(parenthesis)
            else:
                if not stack or lookup[stack.pop()]!=parenthesis:
                    return False
                else:
                    continue
        return False if stack else True

# 利用栈来匹配后面的符号    
        
   