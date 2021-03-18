class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        while slow<len(nums) and nums[slow]!=0:
            slow+=1
        for fast in range(slow,len(nums)):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
        
    #双指针，slow指向0，fast指向非0.都从左出发