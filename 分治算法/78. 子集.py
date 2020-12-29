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