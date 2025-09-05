class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_i,res_j = 0,0
        for i in range(len(s)):
            res_i,res_j = self.extend(i,i,s,res_i,res_j)
            res_i,res_j  = self.extend(i,i+1,s,res_i,res_j)
        return s[res_i:res_j+1]
    
    def extend(self,l,r,s,res_i,res_j):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        if r-l-2>res_j-res_i:
            return l+1,r-1
        return res_i,res_j
       
# 从中间往两边扩展，两种情况:1. 中间单独aba 2.中间一对 baab
# 时间复杂度:O(n^2) 空间:O(1)
