class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # ()(()
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res,i-stack[-1])
                else:
                    stack.append(i)
        return res
#https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
# 初始化栈为-1

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp=[0]*len(s)
        for i in range(len(s)):
            if s[i]==')':
                if i-1>=0:
                    if s[i-1]=='(':
                        if i-2>=0:
                            dp[i]=2+dp[i-2]
                        else:
                            dp[i]=2
                    else:
                        if i-dp[i-1]-1<0:
                            continue
                        else:
                            if s[i-dp[i-1]-1]==')':
                                continue
                            else:
                                if i-dp[i-1]-2<0:
                                    dp[i]=2+dp[i-1]
                                else:
                                    dp[i]=2+dp[i-1]+dp[i-dp[i-1]-2]
        return max(dp)
# dp
#笔记
#https://leetcode-cn.com/problems/longest-valid-parentheses/solution/shou-hua-tu-jie-zhan-de-xiang-xi-si-lu-by-hyj8/
