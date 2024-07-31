class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 4 3 2 1
        # 1 4 5 3 2 
        index=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i 
                break
        if index==-1:
            return self.reverse(nums,0,len(nums)-1)

        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[index]:
                nums[i],nums[index]=nums[index],nums[i]
                break
        self.reverse(nums,index+1,len(nums)-1)

    def reverse(self,nums,l,r):
        while r>l:
            nums[l],nums[r]=nums[r],nums[l]
            r-=1
            l+=1
#https://www.youtube.com/watch?v=IbcQOdtmvpA

# new code，找交换位置的时候可以用binary search找upper bound。On + Ologn = On，并未快多少，但是代码不好写，建议上边那种写法。
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = float('-inf')
        target_index = None
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>=prev:
                prev = nums[i]
            else:
                target_index = i 
                break
        if target_index is None:
            self.reverse(nums, 0, len(nums)-1) 
            return 
        gt_target_index = self.bsearch(nums, target_index+1, len(nums),nums[target_index])
        nums[target_index], nums[gt_target_index] = nums[gt_target_index], nums[target_index]
        self.reverse(nums, target_index+1, len(nums)-1)

    def reverse(self, nums, l, r):
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1

    def bsearch(self, nums, l, r, target):
        while l<r:
            m = (l+r-1)//2
            if nums[m]>target:
                l = m+1
            else:
                r = m
        return l-1
