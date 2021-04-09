class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.upperBound(nums,target)-self.upperBound(nums,target-1)

    def upperBound(self,nums,target):
        l,r=0,len(nums)
        while l<r:
            m=(l+r-1)//2
            if nums[m]<=target:
                l=m+1
            if nums[m]>target:
                r=m
        return l 
#找出target的upperbound，找出target-1的upperbound，相减。
#nums = [5,7,7,8,8,10], target = 8  upperbound指向10
#nums = [5,7,7,8,8,10], target = 7  upperbound指向8，相减即可。
#即使target-1不再数组里，同样适用。
#nums = [5,6,6,8,8,10], target = 8  upperbound指向10
#nums = [5,6,6,8,8,10], target = 7  upperbound还是指向8，相减即可。

'''
1. 二分查找要求数组是排序的，数组可以有repeat的元素。
   例如:[1,1,1,3,4,4] targer=3 用二分查找可以找到3。

2. 当数组内没有target时，l指针最终会指向比target刚好大的数。
   例如: [1,2,4,5] target=3。最终l会指向4。

3. upperbound: 严格>target的数。 
    if nums[m]<=target: l=m+1 等于target的情况，往右走
    if nums[m]>target: r=m
    最终l指向upperbound。  

    lowerbound：>=target的数。
    if nums[m]<target:l=m+1
    if nums[m]>=target:r=m  等于target的情况，往左走
    最终l指向lowerbound。
   例如: [1,1,2,3,3,3,4] target=3，lowerbound=3，upperbound=4.

'''