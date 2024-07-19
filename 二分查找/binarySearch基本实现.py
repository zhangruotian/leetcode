def binarySearch(nums,target):
    l=0
    r=len(nums)            #[l,r) 保持一致 bugfree
    while l<r:
        m=(l+r-1)//2
        if nums[m]==target:
            return True
        elif nums[m]<target:
            l=m+1          #[l,r) 保持一致 bugfree
        else:
            r=m          #[l,r) 保持一致 bugfree
    return False
# 如果未找到target，最后ij重合退出循环，而且ij指向的位置是target应该插入的位置。 1 2 4 target3， ij=2， 1 2 3 target4， ij=3.



def binarySearchRec(nums,target):
    l = 0
    r = len(nums)
    m = (l + r - 1) // 2
    if nums==[]:
        return False
    if nums[m] == target:
        return True
    if nums[m] < target:
        return binarySearchRec(nums[m+1:r],target)
    else:
        return binarySearchRec(nums[0:m],target)


nums=[12,15,17,19,21,24,45]
target=45
print(binarySearchRec(nums,target))

# https://www.nowcoder.com/practice/4f470d1d3b734f8aaf2afb014185b395?tpId=188&&tqId=38588&rp=1&ru=/activity/oj&qru=/ta/job-code-high-week/question-ranking
# 请实现有重复数字的升序数组的二分查找
# 给定一个 元素有序的（升序）长度为n的整型数组 nums 和一个目标值 target，写一个函数搜索 nums 中的第一个出现的target，如果目标值存在返回下标，否则返回 -1
class Solution:
    def search(self , nums: List[int], target: int) -> int:
        # write code here
        if not nums: return -1
        l,r = 0, len(nums)
        while l<r:
            m = (l+r-1)//2
            if nums[m]>= target:
                r=m
            else:
                l = m+1
        return l if nums[l]==target else -1
# 小于或者等于的时候往左搜，最后ij落在的位置就是第一个target（nums中有target的情况下）。如果没有ij会落在稍大的位置，这时候代码也会返回index，但是应该返回-1，所以加一个
# 判断 return l if nums[l]==target else -1
