class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        multi=""
        res=""
        for c in s:
            if c.isdigit():
                multi+=c
            if c.isalpha():
                res+=c
            if c=="[":
                stack.append((res,int(multi)))
                res=""
                multi=""
            if c=="]":
                tmp_s,tmp_mul=stack.pop()
                res=tmp_s+tmp_mul*res
        return res 