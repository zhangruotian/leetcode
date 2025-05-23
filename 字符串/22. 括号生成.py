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
        res=[]
        self.helper(n-1,n,'(',res)
        return res
    
    def helper(self,l,r,item,res):
        if r==0:
            res.append(item)
        if l>0:
            self.helper(l-1,r,item+'(',res)
        if l<r:
            self.helper(l,r-1,item+')',res)

# 回溯算法(深度优先遍历)。判断可加左括号条件：l有剩余
  #     判断可加右括号条件：r有剩余且剩余的l<r。只要有剩余就能加'('，但是')'不能比'('先出现
  
