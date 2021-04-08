class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat=set()
        max_val,min_val=0,14
        for num in nums:
            if num==0:
                continue
            if num in repeat:
                return False
            repeat.add(num)
            max_val=max(num,max_val)
            min_val=min(num,min_val)
        return max_val-min_val<5
# 是顺子的条件
#1. 除0之外的数字无重复
#2. max-min<5
# T:O(n)