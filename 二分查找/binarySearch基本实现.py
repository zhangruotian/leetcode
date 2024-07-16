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
