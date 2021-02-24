class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        res=n
        sums=[0]*n
        sums[0]=nums[0]
        for i in range(1,n):
            sums[i]=sums[i-1]+nums[i]
        for i in range(0,n):
            if i==0:
                j=self.lowerBound(sums,target)
            else:
                j=self.lowerBound(sums,target+sums[i-1])
            if j!=n:
                res=min(res,j-i+1) #注意没找到时不能算
        return res

    
    def lowerBound(self,sums,target):
        l,r=0,len(sums)
        while l<r:
            m=(l+r-1)//2
            if sums[m]>=target:
                r=m
            else:
                l=m+1
        return l
# 二分查找 nlogn

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,sum,res=0,0,float(inf)
        for j in range(len(nums)):
            sum+=nums[j]
            while sum>=target:
                res=min(res,j-i+1)
                sum-=nums[i]
                i+=1
        return 0 if i==0 else res
# 滑动窗口  O(n)
#https://www.youtube.com/watch?v=jp15K7dTCHc
# 注意实现时代码别写的冗长