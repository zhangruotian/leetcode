class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=['(']*n+[')']*n
        path,res,visited=[],[],[0]*len(l)
        self.backTrack(l,path,res,visited,0,len(l))
        return res
    
    def backTrack(self,l,path,res,visited,nums_left,n):
        if nums_left<0:
            return
        if len(path)==n and not nums_left:
            res.append(''.join(path[:]))
            return 
        for i in range(len(l)):
            if visited[i]:continue
            if l[i-1]==l[i] and not visited[i-1]:
                continue
            path.append(l[i])
            visited[i]=1
            if l[i]=='(':
                self.backTrack(l,path,res,visited,nums_left+1,n)
            else:
                self.backTrack(l,path,res,visited,nums_left-1,n)
            visited[i]=0
            path.pop()
#visited过的跳过
#l[n]==l[n-1]且没有visited过的跳过，防止重复
#如果先出现')'是错误的，直接return

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