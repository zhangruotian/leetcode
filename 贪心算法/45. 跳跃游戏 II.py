class Solution:
    def jump(self, nums: List[int]) -> int:
        i = -1
        max_reach = 0
        res = 0
        while max_reach<len(nums)-1:
            new_max_reach = max_reach
            for j in range(i+1,max_reach+1):
                new_max_reach = max(new_max_reach,nums[j]+j)
            i = max_reach
            max_reach = new_max_reach
            res+=1
        return res
# greedy，每一跳记录不同位置能到达最远的位置，直到到达len(nums)-1。O(n)
