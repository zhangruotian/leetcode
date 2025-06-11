class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        c = Counter(t)
        formed = 0
        i = 0
        res_i,res_j = 0,0
        res_len = float('inf')
        for j in range(len(s)):
            if s[j] in c: 
                if c[s[j]]>0:
                    formed+=1
                c[s[j]]-=1
            while formed == len(t):
                if j-i+1<res_len:
                    res_len = j-i+1
                    res_i,res_j = i,j
                if s[i] in c:
                    if c[s[i]]>-1:
                        formed-=1
                    c[s[i]] += 1
                i+=1
        return "" if res_len == float('inf') else s[res_i:res_j+1]

            #https://www.youtube.com/watch?v=YP3bBDuojqk
