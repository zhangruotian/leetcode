class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        res=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j] and res[j]+1>res[i]:
                    res[i]=res[j]+1

        return max(res)
        
# T:O(n^2) S:O(n)
# youtube.com/watch?v=fV-TF4OvZpk