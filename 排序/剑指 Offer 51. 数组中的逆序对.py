class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:return 0
        self.res=0
        self.mergeSort(nums,0,len(nums))
        return self.res

    def merge(self,nums1,nums2):
        n1,n2=len(nums1),len(nums2)
        res=[]
        i,j=0,0
        while i<n1 and j<n2:
            if nums1[i]<=nums2[j]:
                res.append(nums1[i])
                i+=1
                self.res+=j
            else:
                res.append(nums2[j])
                j+=1
        for x in range(j,n2):
            res.append(nums2[x])
        for x in range(i,n1):
            res.append(nums1[x])
            self.res+=j
        return res
    
    def mergeSort(self,nums,l,r):
        if l+1==r:
            return [nums[l]]
        m=(l+r-1)//2
        left=self.mergeSort(nums,l,m+1)
        right=self.mergeSort(nums,m+1,r)
        return self.merge(left,right)

#https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
        
