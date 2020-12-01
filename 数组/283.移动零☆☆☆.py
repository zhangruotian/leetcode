class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_point=0
        for fast_point in range(len(nums)):
            if nums[fast_point] !=0:
                nums[slow_point],nums[fast_point]=nums[fast_point],nums[slow_point]
                slow_point+=1
             
# 双指针
# 维护fast_point与slow_point两个指针，如果nums[fast_point]不为0，则交换nums[fast_point]与nums[slow_point]。保证把0放在后面。
# 时间复杂度O(n),空间复杂度O(1)