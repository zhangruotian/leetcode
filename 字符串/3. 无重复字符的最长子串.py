class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #bcadab
        d = {}
        i = 0
        res = 0
        for j in range(len(s)):
            if s[j] in d and d[s[j]]+1>i:
                i = d[s[j]]+1
            res = max(res,j-i+1)
            d[s[j]] = j
        return res

# 滑动窗口 T:O(n)
# https://www.youtube.com/watch?v=LupZFfCCbAU
