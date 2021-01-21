class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        while True:
            while l<len(nums) and nums[l]%2==1:
                l+=1
            while r>0 and nums[r]%2==0:
                r-=1

            if l>=r:
                break
            nums[r],nums[l]=nums[l],nums[r]
        return nums
# 前后双指针