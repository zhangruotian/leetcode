class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(1,len(nums)+1):
            res^=i
        for n in nums:
            res^=n
        return res
# 与136之出现一次的数一样
# [0,1,3]缺少2,与0，1，2，3异或即可。2是只出现一次的数。
#  0^1^3^0^1^2^3 =2

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int(len(nums)*(len(nums)+1)/2-sum(nums))
# 算出0~n的和，减去nums的和即可
# (0+n)*n/2 - sum(nums)