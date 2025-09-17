class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 100 第一种情况，前后不挨着
        # 1 2 第二种情况，3来了，前面挨着 把dict中改成 1:3 3:3，2不用管
        # 2 3 第三种情况，1来了，后面挨着 把dict中改成 1:3 3:3，2不用管
        # 1 2 4 5 第四种情况，3来了，前后都挨着，把dict中改成 1:5 5:5，234都不用管
        # 最后找dict的values中的最大值
        nums = set(nums)
        d = {}
        for num in nums:
            if (not num-1 in d) and (not num+1 in d):
                d[num]=1
            elif (not num-1 in d) and (num+1 in d):
                cur_len = d[num+1]
                d[num] = cur_len+1
                d[num+cur_len] = cur_len+1
            elif (num-1 in d) and (not num+1 in d):
                cur_len = d[num-1]
                d[num] = cur_len+1
                d[num-cur_len] = cur_len+1
            else:
                cur_len_left = d[num-1]
                cur_len_right = d[num+1]
                d[num-cur_len_left] = cur_len_left+cur_len_right+1
                d[num+cur_len_right] = cur_len_left+cur_len_right+1
        return max(d.values()) if d else 0



        
        
        
