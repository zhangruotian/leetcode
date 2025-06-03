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


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2 3 4 5
        #  3 4 5 2
        #  1 2 4 5 3
        if not nums:
            return 0
        d = {}
        nums=set(nums)
        for num in nums:
            if num-1 not in d and num+1 not in d:
                d[num]=1
            if num-1 in d and num+1 in d:
                length = d[num-1]+d[num+1] +1
                d[num-d[num-1]] = length
                d[num+d[num+1]] = length
                continue
            if num-1 in d:
                length = d[num-1]+1
                d[num] = length
                d[num-d[num-1]] = length
            if num+1 in d:
                length = d[num+1]+1
                d[num] = length
                d[num+d[num+1]] = length
        return max(d.values())


        
        
        
