class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.mergeSort(nums,0,len(nums)-1)[-k]
    
    def merge(self,nums1,nums2):
        #1 2
        n1,n2=len(nums1),len(nums2)
        res=[]
        p1,p2=0,0
        while p1<n1 and p2<n2:
            if nums1[p1]<nums2[p2]:
                res.append(nums1[p1])
                p1+=1
            else:
                res.append(nums2[p2])
                p2+=1
        for i in range(p1,n1):
            res.append(nums1[i])
        for i in range(p2,n2):
            res.append(nums2[i])
        return res
    
    def mergeSort(self,nums,l,r):
        if l==r:
            return [nums[l]]
        m=(l+r-1)//2
        l=self.mergeSort(nums,l,m)
        r=self.mergeSort(nums,m+1,r)
        return self.merge(l,r)