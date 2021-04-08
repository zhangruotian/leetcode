class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_area=0
        while l!=r:
            area=min(height[l],height[r])*(r-l)
            if area>max_area:
                max_area=area
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return max_area
        
#双指针法，前后放置指针。短板决定水高，因此移动较短的指针，左侧向右，右侧向右，直到相遇。
#如果移动较高指针，后面所有的面积都会比当下的面积小。我们要找最大的，因此应移动较矮的指针。
# 时间复杂度O(n)，空间复杂度O(1)