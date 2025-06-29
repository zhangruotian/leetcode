class Solution:
  
    def encode(self, strs: List[str]) -> str:
        encoded=''
        for s in strs:
            encoded += str(len(s))+'#'+s
        return encoded
      
    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            new_i=self.getstr(s,i,res)
            i = new_i
        return res
      
    def getstr(self,s,i,res):
        num = 0
        while i<len(s):
            c = s[i]
            if c.isdigit():
                num = num*10+int(c)
            if c=='#':
                break
            i+=1
        res.append(s[i+1:i+1+num])
        return i+1+num
      
# https://www.youtube.com/watch?v=B1k_sxOSgv8
