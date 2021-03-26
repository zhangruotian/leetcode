class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:return 0
        if s[0]=="0":return 0
        if len(s)==1:return 1
        dp=[0]*len(s)
        dp[0]=1
        if int(s[:2])>=10 and int(s[:2])<=26 and s[1]!="0":
            dp[1]=2
        elif s[1]=="0" and int(s[:2])>26:
            dp[1]=0
        else:
            dp[1]=1
        for i in range(2,len(s)):
            a=dp[i-1] if s[i]!="0" else 0
            b=dp[i-2] if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26 else 0
            dp[i]=a+b
        return dp[-1]

#dp[i]=dp[i-1]+dp[i-2]  如果有的话，可能两项都为0