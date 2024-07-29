class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2=len(nums1),len(nums2)
        if n1>n2:return self.findMedianSortedArrays(nums2,nums1)  #保证num1较短，T:O(log(min(n,m)))
        l,r=0,n1   # 二分查找模板，[l,r)
        k=(n1+n2+1)//2  # 合并后的列表左侧有k个元素。n1+n2=7 k=4 左侧有4元素 右侧3元素。 n1+n2=8 k=4 左侧有4元素 右侧4元素。
        min_val,max_val=float(-inf),float(inf)
        while l<r:
            i=l+(r-l)//2  #找nums1中间偏右的索引。 l+r=4 i=2; l+r=3 i=1。 同时可表示num1为合并后的列表左侧贡献i个元素。
            j=k-i         #nums2中间偏右的索引。同时可表示num2为合并后的列表左侧贡献j个元素。
            if nums1[i]<nums2[j-1]:                 #如果nums1右侧的元素比num2左侧小，说明要从nums1右边找。相反从左边找。
                l=i+1     # 二分模板 [l,r)          #类似找lower_bound，找到nums1[i]刚好比nums2[j-1]大的i，就是最后的位置。
            else:                                   #l最后的位置就是我们要找的位置。
                r=i       # 二分模板 [l,r)
        r1=l  #nums1的r的位置
        r2=k-l  #nums2的r的位置
        nums1_l=nums1[r1-1] if r1>=1 else min_val   #如果r<=0，r-1会越界。此时情况：# | 1 2       此时合并的列表左侧只需看6
        nums2_l=nums2[r2-1] if r2>=1 else min_val                                   # 4  5 6| 7
        median_l=max(nums1_l,nums2_l)           #median左侧
        if (n1+n2)%2!=0:
            return median_l
        nums1_r=nums1[r1] if r1<n1 else max_val
        nums2_r=nums2[r2] if r2<n2 else max_val
        median_r=min(nums1_r,nums2_r)           #median右侧
        return (median_l+median_r)/2

# T:O(log(min(m,n)))

# new code
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if not nums1 and not nums2: return None
        if not nums1: 
            return nums2[n2//2] if n2%2==1 else (nums2[n2//2-1]+nums2[n2//2])/2
        if not nums2:
            return nums1[n1//2] if n1%2==1 else (nums1[n1//2-1]+nums1[n1//2])/2
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        l,r = -1, n1
        while l<r:
            l1_index = (l+r-1)//2
            r1_index = l1_index+1
            l2_index = (n1+n2-1)//2-l1_index-1
            r2_index = l2_index+1
            if r1_index == n1 or nums2[l2_index]>nums1[r1_index]:
                l = l1_index+1
            elif l1_index == -1 or nums1[l1_index]>nums2[r2_index]:
                r = l1_index 
            else:
                break
        l1 = nums1[l1_index] if -1<l1_index<n1 else float('-inf')
        r1 = nums1[r1_index] if -1<r1_index<n1 else float('inf')
        l2 = nums2[l2_index] if -1<l2_index<n2 else float('-inf')
        r2 = nums2[r2_index] if -1<r2_index<n2 else float('inf')
        if (n1+n2)%2 == 1:
            return max(l1,l2)
        else:
            return (max(l1,l2)+min(r1,r2))/2
