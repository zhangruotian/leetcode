class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        self.dfs(nums,res,path,0,target)
        return res
    
    def dfs(self,nums,res,path,index,target):
        if sum(path)==target:
            res.append(path[:])
            return 
        if sum(path)>target:
            return 
        for i in range(index,len(nums)):
            path.append(nums[i])
            self.dfs(nums,res,path,i,target)
            path.pop()