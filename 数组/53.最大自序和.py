class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr=[0]*len(nums)
        arr[0]=nums[0]
        for i in range(1,len(nums)):
            A = nums[i]
            B = nums[i]+arr[i-1]
            arr[i]=max(A,B)
        return max(arr)
        
# 动态规划:
# 1.分析，找出递归方程： OPT(i)表示 末尾为第i个元素时的子序列的最优解，即最大值。
# 分析可知，有两种情况：a. 只选当前值nums[i]  (OPT(i-1)可能为负数)
#                       b. 选 OPT(i-1)+nums[i]
#                       所以递归方程为OPT(i)=max(nums[i],OPT(i-1)+nums[i])
# 2. 找到出口。OPT(0)=nums[0]
# 3. 动态规划:用list记录OPT(0)---OPT(n)
# 4. return list的最大值
# O(n)
