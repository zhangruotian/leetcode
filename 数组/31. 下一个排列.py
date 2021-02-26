class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        i=len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i==-1:
            self.reverse(nums,0,len(nums)-1)
        else:
            j=len(nums)-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
            self.reverse(nums,i+1,len(nums)-1)

    def reverse(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
#https://www.youtube.com/watch?v=IbcQOdtmvpA