class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path=[]
        res=[]
        visited=[0]*len(nums)
        nums.sort()
        self.backTrack(nums,path,res,visited,0)
        return res
    
    def backTrack(self,nums,path,res,visited,index):
        res.append(path[:])
        if index==len(nums):
            return
        for i in range(index,len(nums)):
            if i>=1 and nums[i]==nums[i-1] and not visited[i-1]:
                continue
            path.append(nums[i])
            visited[i]=1
            self.backTrack(nums,path,res,visited,i+1)
            path.pop()
            visited[i]=0
# backtrack
# 用visited记录是否被访问过。如果nums[i]==nums[i-1]而且visited[i-1]为false，则continue