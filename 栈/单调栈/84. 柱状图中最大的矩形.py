class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        left_stack = [0]
        extend_left = [i for i in range(n)]
        for i in range(1,n):
            while left_stack and heights[left_stack[-1]]>=heights[i]:
                left_stack.pop()
            if left_stack:
                extend_left[i] = left_stack[-1]+1
            else:
                extend_left[i] = 0
            left_stack.append(i) 

        right_stack = [n-1]
        extend_right = [i for i in range(n)]
        for i in range(n-2,-1,-1):
            while right_stack and heights[right_stack[-1]]>=heights[i]:
                right_stack.pop()
            if right_stack:
                extend_right[i] = right_stack[-1]-1
            else:
                extend_right[i] = n-1
            right_stack.append(i) 
        
        for i in range(n):
            res = max(res,heights[i]*(extend_right[i]-extend_left[i]+1))
        return res 
# 单调栈
# 核心思想: 对于直方图中的每一个柱子 i，你想找到以它自身高度 heights[i] 为准，能向左和向右延伸的最大宽度。宽度就是 右边界 - 左边界 + 1。

# 实现方式：
# 第一次遍历 (从左到右)：使用 left_stack 找到了每个柱子 i 的左边界 extend_left[i]。
# 第二次遍历 (从右到左)：使用 right_stack 找到了每个柱子 i 的右边界 extend_right[i]。
# 第三次遍历：根据预计算好的左右边界，计算每个柱子能构成的最大矩形面积，并找出全局最大值。
