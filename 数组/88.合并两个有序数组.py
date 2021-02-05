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

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=m-1
        p2=n-1
        p=m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1]>=nums2[p2]:
                nums1[p]=nums1[p1]
                p1-=1
            else:
                nums1[p]=nums2[p2]
                p2-=1
            p-=1
        nums1[:p2+1]=nums2[:p2+1]
# 定义三个指针，一个p1指向nums1的第m-1 ，一个p2指向nums2的第n-1，一个p指nums1的最后
# 那个大就添加到p
# 某个到了-1就把另一个的剩余添加到nums1
# O(m+n)
# O(1)