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

#不用split, t:o(max(m,n)) , s:o(1)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1,p2=0,0
        while p1!=-1 or p2!=-1:
            p1,n1=self.getNext(version1,p1)
            p2,n2=self.getNext(version2,p2)
            if n1<n2:
                return -1
            if n1>n2:
                return 1
        return 0

    def getNext(self,version,p):
        # 01.01.01. 001.001.001
        if p==-1:
            return -1,0
        next=""
        while version[p]!='.':
            if p==len(version)-1:
                return -1,int(next+version[p])
            next+=version[p]
            p+=1
        return p+1,int(next)
        