class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        res=[0]*length
        res[0]=1
        for i in range(1,length):
            res[i]=res[i-1]*nums[i-1]
        right=1
        for j in reversed(range(length)):
            res[j]=res[j]*right
            right=right*nums[j]
        return res
        
# 两次循环: 一次把num[i]左边的数乘起来，一次把num[i]右边的数乘起来
# 原数组：       [1       2       3       4]
# 左部分的乘积：   1       1      1*2    1*2*3
# 右部分的乘积： 2*3*4    3*4      4      1
# 结果：        1*2*3*4  1*3*4   1*2*4  1*2*3*1
# 时间复杂度O(n),空间复杂度O(n),不算返回列表空间复杂度O(1)