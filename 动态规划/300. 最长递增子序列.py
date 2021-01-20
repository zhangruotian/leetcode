class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        res=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j] and res[j]+1>res[i]:
                    res[i]=res[j]+1

        return max(res)
        
# T:O(n^2) S:O(n)
# youtube.com/watch?v=fV-TF4OvZpk

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            if not res or i>res[-1]:
                res.append(i)
            else:
                self.lower_bound(res,i)
        return len(res)

    def lower_bound(self,nums,x):
        l=0
        r=len(nums)
        while l<r:
            m=(l+r-1)//2
            if nums[m]<x:
                l=m+1
            else:
                r=m
        nums[l]=x
# res[]里面放到目前为止的最优序列（可能不属于sub sequence，但是长度结果是正确的）
# 方法：如果新值大于res[-1]，res接上
# 如果新值小于或等于res[-1],二分查找 lower_bound,替换res[x]。

# lower_bound: [1,3,5]中找4，则返回5。找3,返回3.
# upper_bound: [1,3,5]中找4，则返回5。找3,返回5.

# T:O(nlog(n)) S:O(n)

#https://www.youtube.com/watch?v=l2rCz7skAlk