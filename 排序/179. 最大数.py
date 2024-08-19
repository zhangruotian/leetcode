# quicksort
# define a compare func

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        l,r = 0, len(nums)-1
        self.quickSort(nums,l,r)
        return str(int(''.join(nums)))
    
    def compare(self,num1,num2):
        return num1+num2<num2+num1 
    
    def quickSort(self,nums,l,r):
        if l>=r:
            return 
        mid = self.partition(nums,l,r)
        self.quickSort(nums,l,mid-1)
        self.quickSort(nums,mid+1,r)
    
    def partition(self,nums,left,right):
        pivot = nums[left]
        l,r = left+1,right
        while True:
            while l<=right and self.compare(pivot,nums[l]):
                l+=1
            while r>left and not self.compare(pivot,nums[r]):
                r-=1
            if l<r:
                nums[l],nums[r] = nums[r],nums[l]
            else:
                break
        nums[left],nums[r] = nums[r],nums[left]
        return r

