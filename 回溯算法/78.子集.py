class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #.  1.   2.   3 
        #. 2 3.  3
        # 3
        path,res = [],[[]]
        self.dfs(nums,path,res,0)
        return res
    
    def dfs(self,nums,path,res,index):
        for i in range(index,len(nums)):
            path.append(nums[i])
            res.append(path[:])
            self.dfs(nums,path,res,i+1)
            path.pop()
