class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)
        while l<r:
            m=(l+r-1)//2
            if nums[m]<nums[r-1]:
                r=m+1
            elif nums[m]>nums[r-1]:
                l=m+1
            else:
                return nums[l]
                
# 往左查找时记得包括当前
# 最后剩下两个元素比较，[1,2] 如果L为1，则不动；[2,1] L为2 右移。 最终两个相同比较，return L即可。

# 二分查找要想：1. 什么条件往左边找，什么条件往右边找。
#               2. 最后时刻，是当前的L与target比，还是自己nums中两个元素比。 分析确定L指向什么。