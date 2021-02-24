class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower=self.lowerBound(nums,target,0,len(nums))
        upper=self.upperBound(nums,target,0,len(nums))
        if upper-lower==0:
            return [-1,-1]
        else:
            return [lower,upper-1]

    def lowerBound(self,nums,target,left,right):
        l,r=left,right
        while l<r:
            m=(l+r-1)//2
            if nums[m]>=target:
                r=m
            else:
                l=m+1
        return l
    
    def upperBound(self,nums,target,left,right):
        l,r=left,right
        while l<r:
            m=(l+r-1)//2
            if nums[m]>target:
                r=m
            else:
                l=m+1
        return l
# lower_bound: >=target的第一个元素位置
# upper_bound: >target的第一个元素位置