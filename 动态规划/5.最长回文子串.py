class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        start=0
        end=0
        length=0
        def getIndex(l,r):
            while l>=0 and r<=n-1 and s[l]==s[r]:
                l-=1
                r+=1
            return l+1,r-1

        for i in range(n):
            single_l,single_r=getIndex(i,i) 
            double_l,double_r=getIndex(i,i+1)
            single_length=single_r-single_l
            double_length=double_r-double_l
            max_length=max(single_length,double_length)
            if max_length>length:
                if single_length>double_length:
                    start=single_l
                    end=single_r
                else:
                    start=double_l
                    end=double_r
                length=max(single_length,double_length)
        return s[start:end+1]
       
# 从中间往两边扩展，两种情况:1. 中间单独aba 2.中间一对 baab