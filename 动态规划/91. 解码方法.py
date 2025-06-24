class Solution:
    def numDecodings(self, s: str) -> int:
        a,b = 1,1
        if s[-1]=="0":
            a=0
        for i in range(len(s)-2,-1,-1):
            if s[i]=='0':
                a,b=0,a
                continue
            tmp = a
            if int(s[i:i+2])<=26:
                a+=b
            b = tmp
        return a


#dp[i]=dp[i-1]+dp[i-2] 如果s[i]和s[i:i+2]符合要求
#值用到了dp[i-1]和dp[i-2]，滚动即可
