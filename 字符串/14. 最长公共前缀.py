class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        i = 0
        while True:
            c = ''
            for word in strs:
                if i>=len(word):
                    return res
                if not c:
                    c = word[i]
                if word[i]!=c:
                    return res
            res+=c
            i+=1
        
