class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre=0
        cur=1
        while len(nums)>cur:
            if nums[cur]==nums[pre]:
                del nums[cur]
            else:
                cur+=1
                pre+=1
        return len(nums)
# O(n) O(1) 前后两个指针