class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))
# set去重，&交集。

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        pointer1=0
        pointer2=0
        res=[]
        while pointer1<len(nums1) and pointer2<len(nums2):
            if nums1[pointer1]==nums2[pointer2]:
                if not res or nums1[pointer1] != res[-1]:   #查看最后一个res元素即可O(1)，无需a in b O(n)
                    res.append(nums1[pointer1])             # A or B 只要 A是true， or后面不会执行，语法错误都没事
                pointer1+=1
                pointer2+=1
            elif nums1[pointer1]<nums2[pointer2]:
                pointer1+=1
            else:
                pointer2+=1
        return res
# 排序，双指针
# tc:O(nlogn+mlogm)