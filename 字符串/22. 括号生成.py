class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ps = ['(',')']
        res, path = [],[]
        self.dfs(ps,res,path,n,n,n)
        return res
    
    def dfs(self,ps,res,path,n,l,r):
        if len(path) == 2*n and l==0 and r==0:
            res.append(''.join(path[:]))
            return
        for i in range(len(ps)):
            if l<0 or r<0:
                continue
            if r<l:
                continue
            path.append(ps[i])
            if ps[i]=='(':
                self.dfs(ps,res,path,n,l-1,r)
            else:
                self.dfs(ps,res,path,n,l,r-1)
            path.pop()
# 回溯

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res,'',n,n)
        return res
    
    def helper(self,res,item,l,r):
        if l<0 or r<0:
            return
        if r<l:
            return 
        if l==0 and r==0:
            res.append(item)
            return
        self.helper(res,item+'(',l-1,r)
        self.helper(res,item+')',l,r-1)
  # 左右括号不能用超，右括号不能比左括号先出现
  
