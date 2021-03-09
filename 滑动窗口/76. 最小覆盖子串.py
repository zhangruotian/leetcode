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