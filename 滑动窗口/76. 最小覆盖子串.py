from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        res_i,res_j = float('-inf'),float('inf')
        i = 0 
        formed = 0
        for j in range(len(s)):
            if s[j] in count:
                count[s[j]]-=1
                if count[s[j]]==0:
                    formed+=1
                while formed==len(count):
                    if j-i<res_j-res_i:
                        res_i,res_j = i,j
                    if s[i] in count:
                        count[s[i]]+=1
                        if count[s[i]]==1:
                            formed-=1
                    i+=1
        return s[res_i:res_j+1] if res_i!=float('-inf') else ''
                
            #https://www.youtube.com/watch?v=YP3bBDuojqk
