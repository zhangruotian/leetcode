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
# t:o(m+n+max(m,n)) s:o(m+n)

#不使用自带函数split,自己实现双指针 t:o(max(m,n)) , s:o(1)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m,n = len(version1),len(version2)
        i,j = 0,0
        while True:
            x = 0
            while i<m and version1[i]!='.':
                x = x*10+ord(version1[i])-ord('0')
                i+=1
            y=0
            while j<n and version2[j]!='.':
                y = y*10+ord(version2[j])-ord('0')
                j+=1
            if x<y:
                return -1
            if x>y:
                return 1
            i+=1
            j+=1
            if i>=m and j>=n:
                return 0
        
