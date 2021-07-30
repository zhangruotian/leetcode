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