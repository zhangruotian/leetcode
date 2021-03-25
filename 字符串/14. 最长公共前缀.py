class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        min_len=float(inf)
        for s in strs:
            if len(s)<min_len:
                min_len=len(s)
        i=0
        res=""
        while i<min_len:
            c=""
            for j,s in enumerate(strs):
                if j==0:
                    c=s[i]
                if s[i]!=c:
                    return res
            res+=c
            i+=1
        return res