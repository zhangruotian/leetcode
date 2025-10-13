class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i in range(n):
            while stack and stack[-1][0]<temperatures[i]:
                _,popped_i = stack.pop()
                res[popped_i] = i-popped_i
            stack.append((temperatures[i],i))
        return res

#单调栈
