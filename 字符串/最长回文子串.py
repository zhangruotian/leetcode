class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        longest_length = -1
        longest_start, longest_end = 0,0
        while i < len(s):
            j = i
            while j<len(s) and s[i]==s[j]:
                j+=1
            j-=1
            start, end=self.extend(s,i,j)
            if end-start>longest_length:
                longest_start, longest_end = start, end
                longest_length = longest_end - longest_start
            i = j+1
        return s[longest_start:longest_end+1]
            
        
    def extend(self, s, i, j):
        while i>=0 and j<len(s) and s[i] == s[j]:
            i-=1
            j+=1
        return i+1,j-1
