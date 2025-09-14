class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=nums[0]
        for i in range(1,len(nums)):
            res=res^nums[i]
        return res
#1. 任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
#2. 任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
#3. 异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。
# 对于一连串的异或来说，可以任意调整他们的位置。

