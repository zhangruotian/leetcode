class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = [0]*(len(nums))
        sums[0] = nums[0]
        res = float('inf')
        for i in range(1,len(nums)):
            sums[i] = sums[i-1]+nums[i]
        for i in range(len(sums)):
            if i ==0:
                j = self.lower_bound(sums,target,i,len(sums))
            else:
                j = self.lower_bound(sums,target+sums[i-1],i,len(sums))
            if j<len(sums):
                res = min(res,j-i+1)
        return 0 if res==float('inf') else res

    def lower_bound(self,sums,target,l,r):
        while l<r:
            m = (l+r-1)//2
            if sums[m]<target:
                l = m+1
            else:
                r=m 
        return l  
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
