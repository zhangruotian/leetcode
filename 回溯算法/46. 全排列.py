class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visited=[0]*len(nums)
        path=[]
        self.backtrack(nums,visited,path,res)
        return res

    def backtrack(self,nums,visited,path,res):
        if len(path)==len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not visited[i]:
                path.append(nums[i])
                visited[i]=1
                self.backtrack(nums,visited,path,res)
                path.pop()
                visited[i]=0
# 回溯算法模板
# https://zhuanlan.zhihu.com/p/93530380

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        self.backtrack(list(reversed(nums)),path,res)
        return res

    def backtrack(self,nums,path,res):
        if len(path)==len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                self.backtrack(nums,path,res)
                path.pop()
# 改进，不需要visited=[]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        n=len(nums)
        if n==1:
            return [nums]
        res=[]
        for i in range(n):
            for j in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+j)
        return res
# 分治