class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res = 0
        while l<r:
            if height[l]<=height[r]:
                res = max(res, (r-l)*height[l])
                l+=1
            else:
                res = max(res, (r-l)*height[r])
                r-=1
        return res
        
#双指针法，前后放置指针。短板决定水高，因此移动较短的指针，左侧向右，右侧向右，直到相遇。
#如果移动较高指针，后面所有的面积都会比当下的面积小。我们要找最大的，因此应移动较矮的指针。
# 时间复杂度O(n)，空间复杂度O(1)

# 正确性证明
# https://leetcode.cn/problems/container-with-most-water/solutions/11491/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
