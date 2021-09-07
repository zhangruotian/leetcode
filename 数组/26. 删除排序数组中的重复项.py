class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         if len(nums)==1:return 1
         i,j=0,1
         res=0
         while j<len(nums):
            if nums[i]==nums[j]:
                 j+=1
            else:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                i+=1
                j+=1
                res+=1
         return res+1
#https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shuang-zhi-zhen-shan-chu-zhong-fu-xiang-dai-you-hu/