class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = [0]*(len(nums)+1)
        for i in range(len(nums)):
            sums[i+1] = nums[i]+ sums[i]
        res = float('inf')
        for i in range(1,len(sums)):
            j = self.bs(sums, sums[i]-target,0,i)
            if j>=0 and j<len(nums):
                res = min(res,i-j)
        return 0 if res==float('inf') else res
    
    def bs(self,nums,target,l,r):
        while l<r:
            m = (l+r-1)//2
            if nums[m]==target:
                return m
            if nums[m]<target:
                l = m+1
            if nums[m]>target:
                r = m
        return l-1
# 二分查找 nlogn

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        sum_ = 0
        i=0
        for j in range(len(nums)):
            sum_+=nums[j]
            while sum_>=target:
                res = min(res,j-i+1)
                sum_-=nums[i]
                i+=1
        return res if res != float('inf') else 0
# 滑动窗口  O(n)
#https://www.youtube.com/watch?v=jp15K7dTCHc
# 注意实现时代码别写的冗长
