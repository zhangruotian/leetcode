class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()   # a=sorted(nums) 会导致空间复杂度O(n)，重新开a空间
        sums=0
        for i in range(0,len(nums),2):    #for i in range(len(nums)):
            sums+=nums[i]                 #     if i %2==0:
        return sums                       #     这种写法计算量为n，左边计算量n/2
# 时间复杂度O(nlog(n))，空间复杂度O(1)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2]) #空间复杂度O(n)