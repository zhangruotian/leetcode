class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for c in s:
            if c.isdigit() or c.isalpha():
                s1+=c
        s1=s1.lower()
        l,r=0,len(s1)-1
        while l<r:
            if s1[l]!=s1[r]:
                return False
            l+=1
            r-=1
        return True