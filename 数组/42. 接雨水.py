class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        length=len(height)
        for i in range(1,length-1):
            max_left=max(height[:i])
            max_right=max(height[i+1:])
            if max_left>height[i] and max_right>height[i]:
                res+=min(max_left,max_right)-height[i]
        return res
# brute force T:O(n^2)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res=0
        n=len(height)
        max_left=[0]*n
        max_right=[0]*n
        max_left[0]=height[0]
        max_right[n-1]=height[n-1]
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],height[i])
        
        for i in range(n-2,-1,-1):
            max_right[i]=max(max_right[i+1],height[i])
        
        for i in range(1,n-1):
            res+=max((min(max_left[i-1],max_right[i+1])-height[i]),0)
        return res
# dp T:O(n) S:O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        n=len(height)
        max_index=0
        max_left=0
        max_right=0
        for i in range(n):
            if height[i]>height[max_index]:
                max_index=i

        for i in range(max_index):
            if height[i]>max_left:
                max_left=height[i]
            else:
                res+=max_left-height[i]

        for i in range(n-1,max_index,-1):
            if height[i]>max_right:
                max_right=height[i]
            else:
                res+=max_right-height[i]
# https://www.youtube.com/watch?v=bu1quf2rOp8
        return res
# 找到最高点，其左边只用看max_left，其右边只用看max_right
# T:O(n) S:O(1)
