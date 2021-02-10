class Solution:
    def longestPalindrome(self, s: str) -> str:
        start,end=0,0
        for i in range(len(s)):
            l1,r1=self.getPalindrome(s,i,i+1)
            l2,r2=self.getPalindrome(s,i,i)
            if r1-l1>=r2-l2 and r1-l1>end-start:
                start,end=l1,r1
            if r2-l2>r1-l1 and r2-l2>end-start:
                start,end=l2,r2
        return s[start:end+1]

    def getPalindrome(self,s,l,r):
        while l>=0 and r<=len(s)-1 and s[l]==s[r]:
            l-=1
            r+=1
        return l+1,r-1
       
# 从中间往两边扩展，两种情况:1. 中间单独aba 2.中间一对 baab
# 时间复杂度:O(n^2) 空间:O(1)