class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AACBD BA k=2
        count = {}
        i = 0
        res = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j],0)+1
            if max(count.values())+k >= j-i+1:
                res = max(res,j-i+1)
            else:
                while i<j and max(count.values())+k < j-i+1:
                    count[s[i]] -= 1
                    i+=1
        return res

# https://www.youtube.com/watch?v=gqXU1UyA8pk
