class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2 1 4 5 3
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                length = 0
                i = 0
                while num+i in nums:
                    length+=1
                    i+=1
                res = max(res,length)
        return res
# https://www.youtube.com/watch?v=rc2QdQ7U78I
# loop through set找下界(num-1不在nums中)，然后依此+1确定长度。不是下界的跳过。


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 100 第一种情况，前后不挨着
        # 1 2 第二种情况，3来了，前面挨着 把dict中改成 1:3 3:3，2不用管
        # 2 3 第三种情况，1来了，后面挨着 把dict中改成 1:3 3:3，2不用管
        # 1 2 4 5 第四种情况，3来了，前后都挨着，把dict中改成 1:5 5:5，234都不用管
        # 最后找dict的values中的最大值
        if not nums:
            return 0
        nums = set(nums)
        d = {}
        for num in nums:
            if num-1 not in d and num+1 not in d:
                d[num] = 1
            if num-1 in d and num+1 in d:
                pre_len_left = d[num-1] 
                pre_len_right = d[num+1]
                d[num-pre_len_left] = pre_len_left+pre_len_right+1
                d[num+pre_len_right] = pre_len_left+pre_len_right+1
                continue
            if num-1 in d:
                pre_len = d[num-1]
                d[num] =pre_len +1
                d[num-pre_len] = pre_len +1
            if num+1 in d:
                pre_len = d[num+1]
                d[num] = pre_len +1
                d[num+pre_len] = pre_len +1 
        return max(d.values())



        
        
        
