class Solution:
    def twoSum(self, nums, target):
        targets={}
        for index,num in enumerate(nums):
            if num in targets:
                return [targets[num],index]
            else:
                targets[target-num]=index
        return None
       
       
# 用hashmap记录下每个元素与target的差值，之后循环的值在hashmap中查找。如何存在，则输出index。否则，继续往hashmap添加。
# 总时间复杂度:O(n)    
# 循环O(n) key in hashmap复杂度O(1) 
# 空间复杂度 ：worst O(n)  average: O(n)