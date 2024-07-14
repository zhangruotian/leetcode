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
        prev_max, res = float('-inf'),float('-inf')
        for i in range(len(nums)):
            prev_max = max(prev_max+nums[i],nums[i])
            res = max(res,prev_max)
        return res
# 空间复杂度O(1)

#followup： 返回子数组，而不是子数组和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res_start, res_end = 0,0
        start, end = 0,0
        prev_max, overall_max = float('-inf'), float('-inf')
        for i in range(len(nums)):
            cur = nums[i]
            if prev_max+cur>cur:
                prev_max = prev_max+cur
            else:
                prev_max = cur
                start = i
            end+=1
            if prev_max > overall_max:
                overall_max = prev_max
                res_start, res_end = start,end
        return nums[res_start:res_end]

#维护一个s记录每个子数组对应的起始index。
#维护start和end记录最大子数组对应的index。当dp比最大值大时，更新start和end
# 最后返回数组即可
