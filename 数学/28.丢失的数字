class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n*(n+1)/2
        cur_sum = 0
        for num in nums:
            cur_sum+=num
        return int(total-cur_sum)
# 数学公式sum(n) = n*(n+1)/2 减去目前arr的和，就是缺失的值。

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [0,1,3,4]
        # [0,1,4,3]
        # [9,6,4,2,3,5,7,0,1]
        # [0,1,2,3,4,5,6,7,9]
        for i in range(len(nums)):
            while nums[i]<len(nums) and nums[i]!=nums[nums[i]]:
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return i+1
# 参考41，把每个元素放到它应该在的位置上
