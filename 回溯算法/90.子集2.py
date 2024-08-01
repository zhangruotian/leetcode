class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,path,visited = [], [], [0]*len(nums)
        self.dfs(nums,res,path,visited,0)
        return res
    
    def dfs(self,nums,res,path,visited,index):
        res.append(path[:])

        for i in range(index,len(nums)):
            if i>0 and nums[i]==nums[i-1] and visited[i-1]==0:
                continue  
            path.append(nums[i])
            visited[i]=1
            self.dfs(nums,res,path,visited,i+1)
            path.pop()
            visited[i]=0
# 用visited记录是否被访问过。如果nums[i]==nums[i-1]而且visited[i-1]为false，则continue
