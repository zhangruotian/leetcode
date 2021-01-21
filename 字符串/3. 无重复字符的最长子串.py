class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,res=0,-1
        lookup={}
        for j in range(0,len(s)):
            if s[j] in lookup:
                if lookup[s[j]]+1>i:
                    i=lookup[s[j]]+1
            lookup[s[j]]=j
            if j-i>res:
                res=j-i
        return res+1

# 滑动窗口 T:O(n)
# https://www.youtube.com/watch?v=LupZFfCCbAU