class Solution:
    def trap(self, height: List[int]) -> int:
        if sum(height) == 0:
            return 0
        res = 0
        heightset_index = -1
        heighest = 0
        l, r = 0, len(height)
        for i in range(l,r):
            if height[i]>heighest:
                heightset_index = i 
                heighest = height[i]

        left_most = 0
        for i in range(heightset_index):
            if height[i]<=left_most:
                res+=left_most-height[i]
            else:
                left_most = height[i]
        right_most = 0
        for i in range(r-1,heightset_index,-1):
            if height[i]<=right_most:
                res+=right_most-height[i]
            else:
                right_most = height[i]
        return res
# https://www.youtube.com/watch?v=bu1quf2rOp8

