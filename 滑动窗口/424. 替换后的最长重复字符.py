class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        count = {s[0]:1}
        i = 0
        for j in range(1,len(s)):
            if s[j] in count:
                count[s[j]]+=1
            else:
                count[s[j]] = 1
            if max(count.values())+k>=j-i+1:
                res = max(res,j-i+1)
            while max(count.values())+k<j-i+1:
                count[s[i]]-=1
                i+=1
        return res

# https://www.youtube.com/watch?v=gqXU1UyA8pk
