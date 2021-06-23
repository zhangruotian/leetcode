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
# 时间复杂度O(n)，空间复杂度O(n)

# 由转移方程可知: OPT(i)只与OPT(i-1)有关，并且最后结果不需要用到所有OPT(i),因此不需要用list记录OPT(0)---OPT(n),用一个variable交替计算即可.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a=nums[0]
        max_value=a
        for i in range(1,len(nums)):
            a = max(nums[i],nums[i]+a)
            if a>max_value:
                max_value=a
        return max_value
# 空间复杂度O(1)

#followup： 返回子数组，而不是子数组和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #返回最大子数组
        #dp[i+1]=max(dp[i]+nums[i+1],nums[i+1])
        s,start,end=0,0,0
        dp=nums[0]
        res=dp
        for i in range(1,len(nums)):
            if dp+nums[i]>=nums[i]:
                dp=dp+nums[i]
            else:
                dp=nums[i]
                s=i
            if dp>res:
                res=dp
                end=i
                start=s
        return nums[start:end+1]
#维护一个s记录每个子数组对应的起始index。
#维护start和end记录最大子数组对应的index。当dp比最大值大时，更新start和end
# 最后返回数组即可
