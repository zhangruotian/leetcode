class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)
        while l<r:
            m=(l+r-1)//2
            if nums[m]<nums[r-1]:
                r=m+1
            elif nums[m]>nums[r-1]:
                l=m+1
            else:
                return nums[l]
                

#  l指向第一个，r-1指向最后一个
# 如果nums[m]>nums[l-1],说明在第一段。往右找，l=m+1
# 如果nums[m]<nums[l-1],说明在第二段，往左找。但是当前的m可能对应最小值，因此r=m+1(搜索区间保留m)
# 如果相等，则区间已缩小到最后，直接return nums[l]