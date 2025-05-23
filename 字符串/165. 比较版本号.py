class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i,j=0,0
        while i<len(version1) or j<len(version2):
            revision1, revision2 = 0,0
            while i<len(version1) and version1[i] != '.':
                revision1 = revision1*10 + ord(version1[i]) - ord('0')
                i+=1
            while j<len(version2) and version2[j] != '.':
                revision2 = revision2*10 + ord(version2[j]) - ord('0')
                j+=1
            if revision1<revision2:
                return -1
            if revision1>revision2:
                return 1
            i+=1
            j+=1
        return 0
