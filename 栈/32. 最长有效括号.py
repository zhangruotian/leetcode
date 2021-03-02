class Solution:
    def longestValidParentheses(self, s: str) -> int:
        self.max_length=0
        stack=[-1]
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            else:
                tmp=stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    length=i-stack[-1]
                    self.max_length=max(self.max_length,length)
        return self.max_length
#https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
# 初始化栈为-1