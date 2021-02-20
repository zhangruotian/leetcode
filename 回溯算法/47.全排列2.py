class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path=[]
        res=[]
        visited=[0]*len(nums)
        nums.sort()
        self.backTrack(path,res,visited,nums)
        return res
    
    def backTrack(self,path,res,visited,nums):
        if len(path)==len(nums):
            res.append(path[:])
            return 
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i>=1 and (nums[i]==nums[i-1] and not visited[i-1]):
                continue
            path.append(nums[i])
            visited[i]=1
            self.backTrack(path,res,visited,nums)
            path.pop()
            visited[i]=0
# 46题用visited记录是否访问过，可以只将不同的数字添加进结果。
# 本题若用上题代码，会出现重复的 比如 112 112
# 只需 添加此条件
#             if i>=1 and (nums[i]==nums[i-1] and not visited[i-1]):
                # continue