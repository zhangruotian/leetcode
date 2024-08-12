class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while i<len(strs[0]):
            prefix  = ''
            for j in range(len(strs)):
                s = strs[j][i] if i<len(strs[j]) else '0'
                if j==0:
                    prefix = s 
                else:
                    if s!=prefix:
                        return strs[0][:i] 
            i+=1
        return strs[0][:i] 
                

