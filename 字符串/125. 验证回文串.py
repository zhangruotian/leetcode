class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        while True:
            while i<len(s) and not s[i].isalnum():
                i+=1
            while j>=0 and not s[j].isalnum():
                j-=1
            if i>=j or i==len(s) or j==-1:
                return True
            a = s[i].lower() if s[i].isalpha() else s[i]
            b = s[j].lower() if s[j].isalpha() else s[j]
            if a!=b:
                return False
            i+=1
            j-=1

# 双指针O(1) space
