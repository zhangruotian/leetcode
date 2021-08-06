class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        step=0
        i=0
        while nums[i]+i<len(nums)-1:
            max_val=float(-inf)
            max_id=0
            for j in range(nums[i]):
                if nums[i+j+1]+j+i+1>max_val:
                    max_id=i+j+1
                    max_val=nums[i+j+1]+j+i+1
            i=max_id
            step+=1
        return step+1
#greedy
#https://leetcode-cn.com/problems/jump-game-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-10/

#dp超时
class Solution:
    def jump(self, nums: List[int]) -> int:
        # for j in range(i):
        #   dp[i]=min(dp[j])+1
        dp=[float(inf)]*len(nums)
        dp[0]=0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]+j>=i:
                    dp[i]=min(dp[j]+1,dp[i])
        return dp[-1]