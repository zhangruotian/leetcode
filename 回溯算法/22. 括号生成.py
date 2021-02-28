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