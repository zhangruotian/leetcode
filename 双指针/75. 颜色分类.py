class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0,p2=-1,len(nums)
        i=0
        while i<p2:
            if nums[i]==0:
                nums[i],nums[p0+1]=nums[p0+1],nums[i]
                p0+=1
            if nums[i]==2:
                nums[i],nums[p2-1]=nums[p2-1],nums[i]
                p2-=1
                i-=1
            i+=1

#指针p0: p0以及p0左侧都为0
#指针p2: p2以及p2右侧都为2
#指针i：扫整个数组，若nums[i]==1，continue
#若nums[i]==0,与p0+1交换，然后p0+=1，i+=1 
#(i与其左侧的元素交换，以及处理过了，因此只有两种情况)
#1.自己跟自己交换。2.自己和1交换。 因此无需对换过来的元素再判断和处理。

#若nums[i]==2,与p2-1交换，然后p2-=1，i-=1,i+=1
#需要重新判断换过来的元素是几，进行相应的处理

#https://www.youtube.com/watch?v=aVOm2Kickys