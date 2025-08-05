class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i in range(n):
            while stack and stack[-1][1]<temperatures[i]:
                popped_i,popped_t = stack.pop()
                res[popped_i] = i-popped_i
            stack.append((i,temperatures[i]))
        return res

#单调栈
#https://www.youtube.com/watch?v=d4FvlTzzWjQ
