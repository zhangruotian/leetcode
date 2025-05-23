class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 1
        # 2 3 4 2
        # 3 2 1
        # 2 9 34 11 3
        if len(nums) == 1: return
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                break
        if i==0 and nums[i]>=nums[i+1]:
            self.reverse(nums,0,len(nums)-1)
            return 
        for j in range(len(nums)-1,i,-1):
            if nums[j]>nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                break
        self.reverse(nums,i+1,len(nums)-1)
    
    def reverse(self,nums,l,r):
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        
