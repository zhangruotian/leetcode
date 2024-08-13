class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                count = 0
                while num in nums:
                    count+=1
                    num+=1
                res = max(res, count)
        return res
# https://www.youtube.com/watch?v=rc2QdQ7U78I
# loop through set找下界(num-1不在nums中)，然后依此+1确定长度。不是下界的跳过。



