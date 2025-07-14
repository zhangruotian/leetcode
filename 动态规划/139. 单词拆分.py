class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for word in wordDict:
                if i-len(word)+1>=0 and dp[i-len(word)+1] and word==s[i-len(word)+1:i+1]:
                    dp[i+1] = True
                    break
        return dp[n]

# https://www.youtube.com/watch?v=H2EgWq-45CY
