class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=dict(collections.Counter(t))
        min_len=float(inf)
        min_str=''
        formed=0
        start=0
        for i in range(len(s)):
            char=s[i]
            if char not in d:
                continue
            d[char]-=1
            if d[char]==0:
                formed+=1
            while formed==len(d) and start<=i:
                #记录结果
                length=i-start+1
                if length<min_len:
                    min_len=length
                    min_str=s[start:i+1]
                #更新start
                left=s[start]
                start+=1
                if left not in d:
                    continue
                d[left]+=1
                if d[left]>0:
                    formed-=1
        return min_str 

            #https://www.youtube.com/watch?v=YP3bBDuojqk

# new code
class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        # ADOBECODEBANC
        count = Counter(t)
        i=0
        while i<len(s) and s[i] not in count:
            i+=1
        if i == len(s):
            return ""
        count[s[i]]-=1
        j = i 
        while j<len(s) and any([val>0 for val in count.values()]):
            j=self.expand(s,j,count)
        if j == len(s):
            return "" if any([val>0 for val in count.values()]) else s[i:j+1]
        print(i,j)
        mini,minj = i,j
        minlen = j-i
        while True:
            i = self.shrink(s,i,j,count)
            if j-i<minlen:
                mini,minj = i,j
                minlen = j-i
            j = self.expand(s,j,count)
            if j == len(s):
                break
        return s[mini:minj+1]
    
    def shrink(self,s,i,j,count):
        while i<j:
            if s[i] in count:
                if count[s[i]]>=0:
                    break
                else:
                    count[s[i]]+=1
            i+=1
        return i 
    
    def expand(self,s,j,count):
        while True:
            j+=1
            if j==len(s):
                return j
            if s[j] in count:
                count[s[j]]-=1
                return j
