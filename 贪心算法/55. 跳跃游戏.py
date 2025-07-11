class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i>reach:
                return False
            reach = max(reach,i+nums[i])
            if reach>=len(nums)-1:
                return True
#如果某一个作为 起跳点 的格子可以跳跃的距离是 3，那么表示后面 3 个格子都可以作为 起跳点。
#可以对每一个能作为 起跳点 的格子都尝试跳一次，把 能跳到最远的距离 不断更新。
#如果可以一直跳到最后，就成功了。

#如果i>reach，代表跳不到i，return false
#如果reach超过了最后index，提前 return true


