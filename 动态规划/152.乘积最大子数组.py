class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minium,maxinum = nums[0],nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            new_minimum = min(minium*num,maxinum*num,num)
            new_maxinum = max(minium*num,maxinum*num,num)
            res = max(res,new_maxinum)
            minium,maxinum = new_minimum,new_maxinum
        return res
