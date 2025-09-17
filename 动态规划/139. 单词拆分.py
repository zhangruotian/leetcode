class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for word in wordDict:
                if i-len(word)+1>=0 and dp[i-len(word)+1] and word==s[i-len(word)+1:i+1]: #注意判断i-len(word)+1>=0
                    dp[i+1] = True
                    break   # 找到某个词可以匹配后，不需要再看别的词了
        return dp[n]

