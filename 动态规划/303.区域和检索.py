class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.arr=self.dp(self.nums)

    def dp(self,nums):
        if len(nums)==0:
            return
        if len(nums) ==1:
            return nums
        arr=[0]*len(nums)
        arr[0]=self.nums[0]
        for x in range(1,len(nums)):
            arr[x]=self.nums[x]+arr[x-1]
        return arr

    def sumRange(self, i: int, j: int) -> int:
        if i>0:
            return self.arr[j]-self.arr[i-1]
        else:
            return self.arr[j]
        
# 动态规划记录从0到i的和f(i)，后面重复调用时可以减小运算量

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(len(self.nums)):
            if i > 0:
                self.nums[i] = self.nums[i]+self.nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        if i>0:
            return self.nums[j]-self.nums[i-1]
        else:
            return self.nums[j]class NumArray:

# 直接在nums上操作，减低空间复杂度（动态规划思想）
