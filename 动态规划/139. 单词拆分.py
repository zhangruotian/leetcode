class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] == 1 and s[j:i] in words:
                    dp[i] = 1
        return True if dp[-1] == 1 else False  

# https://www.youtube.com/watch?v=H2EgWq-45CY
