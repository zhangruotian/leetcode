class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # [1,2]
        # [0,0,1,0,1,0,0]
        # [1]
        # [0,1,0]
        # [1,1,1] target=1
        # [1,0,2,0,2,0,1]
        # [1,0,0] 1
        # [2,0,2]
        # [1,2,1] target=0
        # [0,1,0,1,0,1,0,0,0]
        sum_ = sum(nums)
        if target>sum_ or target<-sum_:
            return 0
        dp_len = 2*sum_+1
        dp = [0]*(dp_len)
        mid = dp_len//2
        dp[mid] = 1

        for num in nums:
            dp_new = [0]*(dp_len)
            for i in range(dp_len):
                if dp[i]!=0:
                    if num==0:
                        dp_new[i] = dp[i]*2
                    else:
                        dp_new[i+num]+=dp[i]
                        dp_new[i-num]+=dp[i]
            dp=dp_new
        return dp[mid+target]
# 能够得到的range为-sum(nums)～sum(nums)。initial 一个长度为这个range的dp数组，dp[i]代表到目前的num为止，i能不能被拼出来。
# 逐渐看更多的num，更新dp，看看哪些值开始可以被拼出来。记得把上的num能拼出来的i set为0，如果当前num不为0的话。
# 注意num=0和!=0的区别处理。
# 不能直接在dp上改，因为改了dp[x]之后，可能从0变成了不是0，会进入循环，导致错误。
