class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.mergeSort(nums,0,len(nums)-1)[-k]
    
    def merge(self, nums1, nums2):
        i, j, k = 0,0,0
        res, len1,len2 = [],len(nums1), len(nums2)
        while i<len1 and j<len2:
            if nums1[i]<=nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        for a in range(i,len1):
            res.append(nums1[a]) 
        for b in range(j,len2):
            res.append(nums2[b])
        return res
    
    def mergeSort(self,nums,l,r):
        if l==r:
            return [nums[l]]
        mid = (l+r)//2
        left=self.mergeSort(nums,l,mid)
        right=self.mergeSort(nums,mid+1,r)
        return self.merge(left,right)
        
        
