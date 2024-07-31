class Solution:
    from collections import Counter
    def generateParenthesis(self, n: int) -> List[str]:
        ps = ["(",")"]
        res, path = [],[]
        self.dfs(ps,path,res,n)
        return res
    
    def dfs(self, ps, path, res, n):
        if len(path)==2*n:
            res.append("".join(path[:]))
            return 

        for i in range(len(ps)):
            count = Counter(path)
            if ps[i]=="(" and count["("]>=n:
                continue
            if ps[i]==")" and count[")"]>=n:
                continue
            if ps[i]==")" and count[")"]==count["("]:
                continue
            path.append(ps[i])
            self.dfs(ps,path,res,n)
            path.pop()
# 回溯

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.helper(res,n,n,'')
        return res
    
    def helper(self,res,l,r,item):
        if l>r:return
        if l==0 and r==0:
            res.append(item)
        if l:
            self.helper(res,l-1,r,item+'(')
        if r:
            self.helper(res,l,r-1,item+')')
#https://www.youtube.com/watch?v=XF0wh8M2A6E
