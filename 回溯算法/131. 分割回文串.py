class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #  a    aa.   aab
        # a ab.  b
        #b
        res,path = [],[]
        self.dfs(s,res,path,0)
        return res
    
    def dfs(self,s,res,path,index):
        if index>=len(s):
            res.append(path[:])
            return
        for i in range(index,len(s)):
            sub_s = s[index:i+1]
            if self.is_palindrome(sub_s):
                path.append(sub_s)
                self.dfs(s,res,path,i+1)
                path.pop()

    def is_palindrome(self,sub_s):
        l,r = 0,len(sub_s)-1
        while l<r:
            if sub_s[l]!=sub_s[r]:
                return False
            l+=1
            r-=1
        return True
