class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1=version1.split(".")
        l2=version2.split(".")
        n1,n2=len(l1),len(l2)
        for i in range(max(n1,n2)):
            bn1=int(l1[i]) if i<n1 else 0
            bn2=int(l2[i]) if i<n2 else 0
            if bn1==bn2:
                continue
            elif bn1>bn2:
                return 1
            else:
                return -1
        return 0
        