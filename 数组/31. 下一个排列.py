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