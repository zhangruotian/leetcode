class Solution:
    def jump(self, nums: List[int]) -> int:
        num_jumps = 0
        last_reached,reached = -1,0
        while reached<len(nums)-1:
            new_reached = reached
            for i in range(last_reached+1,new_reached+1):
                new_reached = max(new_reached, nums[i]+i)
            last_reached = reached
            reached = new_reached
            num_jumps+=1
        return num_jumps
# greedy，每一跳记录不同位置能到达最远的位置，知道到达len(nums)-1。O(n)
