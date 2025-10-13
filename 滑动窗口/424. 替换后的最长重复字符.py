from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AABCACCC 1
        cnt = Counter()
        res = 0
        n = len(s)
        i = 0
        for j in range(n):
            cnt[s[j]]+=1
            while max(cnt.values())+k<j-i+1:
                cnt[s[i]]-=1
                i+=1
            res = max(res,j-i+1)
        return res

# https://www.youtube.com/watch?v=gqXU1UyA8pk
