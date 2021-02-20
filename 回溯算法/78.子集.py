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
        res=[]
        for num in reversed(nums):
            for i in res[:]:
                res.append([num]+i)
            res.append([num])
        res.append([])
        return res
# 直接从后遍历，遇到一个数就把所有子集加上该数组成新的子集，遍历完毕即是所有子集

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
#分治