class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,path,visited = [],[],[0]*len(nums)
        self.dfs(nums,res,path,visited)
        return res
    
    def dfs(self,nums,res,path,visited):
        if sum(visited) == len(nums):
            res.append(path[:])
        for i in range(len(nums)):
            if visited[i]:
                continue
            path.append(nums[i])
            visited[i] = 1
            self.dfs(nums,res,path,visited)
            visited[i] = 0
            path.pop()
# 回溯算法模板
# https://zhuanlan.zhihu.com/p/93530380

