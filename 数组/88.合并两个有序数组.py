class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_m = nums1[:m]
        point_m=0
        point_n=0
        i = 0
        while point_m<len(nums1_m) and point_n<len(nums2):
            if nums1_m[point_m]<=nums2[point_n]:
                nums1[i]= nums1_m[point_m]
                i+=1
                point_m+=1
            else:
                nums1[i]= nums2[point_n]
                i+=1
                point_n+=1
        if point_m==len(nums1_m):
            nums1[i:]=nums2[point_n:]
        else:
            nums1[i:]=nums1_m[point_m:]
         
# 合并两个《有序数组》并得到有序数组，考虑双指针
# 时间复杂度O(m+n)
# 空间复杂度O(m)