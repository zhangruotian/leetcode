class Solution:
    # 1 3 | 5
    #   2 | 4 6

    # 1 3 | 
    #   2 |4 6

    # 1
    # 2 3 4
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1,len2 = len(nums1),len(nums2)
        if len1>len2:
            return self.findMedianSortedArrays(nums2,nums1)
        if len1==0:
            if len2%2==0:
                return (nums2[(len2-1)//2]+nums2[(len2-1)//2+1])/2
            else:
                return nums2[(len2-1)//2]
        l,r = -1,len1
        while l<r:
            m1 = (l+r-1)//2
            nums1_left = nums1[m1] if m1>=0 else float('-inf')
            nums1_right = nums1[m1+1] if m1+1<len1 else float('inf')
            n1 = (len1+len2-1)//2-m1-1
            nums2_left = nums2[n1] if n1>=0 else float('-inf')
            nums2_right = nums2[n1+1] if n1+1<len2 else float('inf')
            if nums1_left<=nums2_right and nums2_left<=nums1_right:
                if (len1+len2)%2==0:
                    return (max(nums1_left,nums2_left)+min(nums1_right,nums2_right))/2
                else:
                    return max(nums1_left,nums2_left)
            if nums1_left>nums2_right:
                r=m1
            if nums2_left>nums1_right:
                l=m1+1
