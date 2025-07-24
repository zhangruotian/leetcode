class Solution:

    def encode(self, strs: List[str]) -> str:
        #[n#e#e#t,c#o#d#e]
        s = ''
        for w in strs:
            s+=str(len(w))+'#'+w
        return s

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i<len(s):
            length = 0
            while s[i].isdigit():
                length = length*10+int(s[i])
                i+=1
            l.append(s[i+1:i+1+length])
            i = i+1+length
        return l
      
# https://www.youtube.com/watch?v=B1k_sxOSgv8
