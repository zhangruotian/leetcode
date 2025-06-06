class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0]=True
        for j in range(1,len(dp)):
            for i in range(j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

# https://www.youtube.com/watch?v=H2EgWq-45CY
