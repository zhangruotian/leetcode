class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path=[]
        res=[]
        self.backTrack(path,res,0,nums)
        return res
    
    def backTrack(self,path,res,index,nums):
        res.append(path[:])
        if index==len(nums):
            return
        for i in range(index,len(nums)):
            path.append(nums[i])
            self.backTrack(path,res,i+1,nums)
            path.pop()
            
# backtrack

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                res.append(res[i]+[num])
        return res
# 直接模拟

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums)==1:
            return [nums,[]] 
        new_list=[]
        num=[nums[0]]
        original_list=self.subsets(nums[1:])
        for i in original_list:
            new_list.append(num+i)
        new_list+=original_list

        return new_list
#divide and conquer
