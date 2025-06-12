class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res_s = self.get_num_palin(s,i,i)
            res_p = self.get_num_palin(s,i,i+1)
            res+=res_s
            res+=res_p
        return res
    
    def get_num_palin(self,s,i,j):
        count = 0
        while i>=0 and j<len(s) and s[i]==s[j]:
            count+=1
            i-=1
            j+=1
        return count

        
