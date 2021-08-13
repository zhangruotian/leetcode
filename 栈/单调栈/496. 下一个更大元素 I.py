class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #[1,2,4,3,2,1,7]
        hashmap={}
        stack=[nums2[0]]
        res=[]
        for i in range(1,len(nums2)):
            if nums2[i]<stack[-1]:
                stack.append(nums2[i])
            else:
                while stack and nums2[i]>stack[-1]:
                    tmp=stack.pop()
                    hashmap[tmp]=nums2[i]
                stack.append(nums2[i])
        for num in nums1:
            if num not in hashmap:
                res.append(-1)
            else: 
                res.append(hashmap[num])
        return res
    #https://leetcode-cn.com/problems/next-greater-element-i/solution/xia-yi-ge-geng-da-yuan-su-i-by-leetcode/