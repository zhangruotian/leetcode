class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path, res = [],[]
        ps = ['(',')']
        self.dfs(ps,path,res,n,n)
        return res
    
    def dfs(self,ps,path,res,l,r):
        if l==0 and r==0:
            res.append(''.join(path))
            return
        if r<l:
            return
        if l<0:
            return 
        for p in ps:
            path.append(p)
            if p=='(':
                self.dfs(ps,path,res,l-1,r)
            if p==')':
                self.dfs(ps,path,res,l,r-1)
            path.pop()
  
