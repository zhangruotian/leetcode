class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=[int(i) for i in str(num)]
        n=len(nums)
        max_index_arr=[0]*n
        max_val,max_index=-1,0
        for i in range(n-1,-1,-1):
            if nums[i]>max_val:
                max_index_arr[i]=i
                max_index=i
                max_val=nums[i]
            else:
                max_index_arr[i]=max_index
        for i in range(0,n):
            if nums[i]<nums[max_index_arr[i]]:
                nums[i],nums[max_index_arr[i]]=nums[max_index_arr[i]],nums[i]
                break
        return int("".join([str(i) for i in nums]))

# 从index=0开始，如果nums[i]大于等于nums[i:]中的最大值，则无需交换
# 如果小于nums[i:]中的最大值，则交换
# 注意交换的时候要交换最后面的，比如1993，1要跟第2个9交换变为9913，如果跟第一个9交换，则9193.
#O(n^2)

#本题先用一个数组从后往前记录最大值的index。可降低为O(n).

        
        