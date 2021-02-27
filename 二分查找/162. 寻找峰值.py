class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r=0,len(nums)
        while l<r:
            m=(l+r-1)//2
            if m+1>=len(nums):  #注意越界处理
                return l
            if nums[m]<nums[m+1]:
                l=m+1
            if nums[m]>nums[m+1]:
                r=m
        return l
# https://www.youtube.com/watch?v=etuTPmks7Dc