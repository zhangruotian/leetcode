class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for j in range(1,n+1):
            for i in range(j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    continue
        return dp[-1]


# https://www.youtube.com/watch?v=H2EgWq-45CY
