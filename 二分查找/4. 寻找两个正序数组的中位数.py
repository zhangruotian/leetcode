class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1),len(nums2)
        if m>n:
            return self.findMedianSortedArrays(nums2,nums1)
        if m==0:
            return nums2[n//2] if n%2 else (nums2[n//2]+nums2[n//2-1])/2
        l,r = -1,m
        while l<r:
            mid = (l+r-1)//2
            left1 = nums1[mid] if mid>=0 else float('-inf')
            right1 = nums1[mid+1] if mid+1<m else float('inf')
            left2_index = (m+n-1)//2-mid-1
            left2 = nums2[left2_index] if left2_index>=0 else float('-inf')
            right2_index = left2_index+1
            right2 = nums2[right2_index] if right2_index<n else float('inf')

            if left1>right2:
                r=mid
            elif left2>right1:
                l=mid+1
            else:
                break

        if (m+n)%2:
            return max(left2,left1)
        return (max(left2,left1)+min(right1,right2))/2
                l=m1+1
