class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        right, left = [n]*n,[-1]*n
        right_stack = [(0,heights[0])]
        left_stack = [(n-1,heights[-1])]
        res = 0
        for i in range(1,n):
            while right_stack and heights[i]<right_stack[-1][1]:
                pop_i,_ = right_stack.pop()
                right[pop_i] = i
            right_stack.append((i,heights[i]))
        
        for i in range(n-2,-1,-1):
            while left_stack and heights[i]<left_stack[-1][1]:
                pop_i,_ = left_stack.pop()
                left[pop_i] = i
            left_stack.append((i,heights[i]))
        
        for i in range(n):
            res = max(res,(right[i]-left[i]-1)*heights[i])
        return res
        
# 单调栈
# 核心思想: 对于直方图中的每一个柱子 i，你想找到以它自身高度 heights[i] 为准，能向左和向右延伸的最大宽度。宽度就是 右边界 - 左边界 + 1。

# 实现方式：
# 第一次遍历 (从左到右)：使用 left_stack 找到了每个柱子 i 的左边界 extend_left[i]。
# 第二次遍历 (从右到左)：使用 right_stack 找到了每个柱子 i 的右边界 extend_right[i]。
# 第三次遍历：根据预计算好的左右边界，计算每个柱子能构成的最大矩形面积，并找出全局最大值。
