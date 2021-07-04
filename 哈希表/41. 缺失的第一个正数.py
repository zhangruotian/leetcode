class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 3 4 -1 1     -1 4 3 1    -1 1 3 4   1 -1 3 4 
        # 1 2 3  4      1 2 3 4.   1. 2 3 4.  1. 2.3 4
        n=len(nums)
        for i in range(n):
            # while是因为交换过来的数依然不在正确位置，继续交换
            # nums[i]!=nums[nums[i]-1] 已经处在正确位置就不交换
            while 1 <= nums[i] <= n and nums[i]!=nums[nums[i]-1]:
                #注意交换代码前后顺序
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        # [1 2 3 4]都不缺，返回5
        return n+1

#T:O(N) S:0(1)
# [3 4 -1 1]的不缺正数形式应为[1 2 3 4] ([1....N] N=nums.length)
# 我们要把每nums的每个数放到正确的位置
# hash function: nums[i]-1，例如 3需要放到index为2的位置
# 最后检验却哪个即可

#nums[1],nums[2]=nums[2],nums[1]
#过程：先生成(nums[2],nums[1])元祖，再解包. nums[1]=nums[2]  nums[2]=nums[1]
#与nums[2],nums[1]=nums[1],nums[2]相同

#此题中之能使用 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
#若 使用nums[i],nums[nums[i]-1]=nums[nums[i]-1],nums[i]则会出错
#生成元祖后 nums[i]=nums[nums[i]-1] 
# nums[nums[i]-1]中的nums[i]已经与原来不同，因为结果错误