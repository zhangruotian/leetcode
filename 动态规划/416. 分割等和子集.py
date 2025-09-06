class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return False
        if sum(nums)%2!=0:
            return False
        half = sum(nums)//2
        dp = [False]*(half+1)
        dp[0] = True
        for num in nums:
            new_dp=dp[:]
            for i in range(1,half+1):
                if i-num>=0 and dp[i-num]:
                    new_dp[i]=True
                if new_dp[-1]==True:
                    return True
            dp = new_dp
        return False
# 跟322 coin change相似，但是那个题每个coin能无限次数使用，本题每个num最多使用一次，把for coin in coins放到外面，能保证每个coin只用一次。
# 注意，eg nums[2,8]，2把dp[2]改了True之后，dp[4]也会得到True，相当于2用了两次，错误。应该对每个来说，都用上个coin的dp结果，而不是当前dp结果。
# https://www.youtube.com/watch?v=z_VLFGzQQtk
