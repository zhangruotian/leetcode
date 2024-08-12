class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)
        while l<r:
            m = (l+r-1)//2
            left = float('-inf') if m-1<0 else nums[m-1]
            right = float('-inf') if m+1>=len(nums) else nums[m+1]
            if left<nums[m]<right:
                l=m+1
            elif left>nums[m]>right:
                r=m
            elif nums[m]>left and nums[m]>right:
                return m
            else:
                r=m
            

