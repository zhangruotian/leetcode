class Solution:
    def jump(self, nums: List[int]) -> int:
        can_reach = 0
        i = 0 
        res = 0
        while can_reach<len(nums)-1:
            new_can_reach=can_reach
            while i<=can_reach:
                new_can_reach = max(new_can_reach,i+nums[i])
                i+=1
            can_reach = new_can_reach
            res+=1
        return res
# greedy，每一跳记录不同位置能到达最远的位置，知道到达len(nums)-1。O(n)
