class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res=[0]*(len(T))
        stack=[]
        for i in range(len(T)):
            while stack and T[i]>T[stack[-1]]:
                tmp=stack.pop()
                res[tmp]=i-tmp
            if not stack or T[i]<=T[stack[-1]]:
                stack.append(i)
        return res

#单调栈
#https://www.youtube.com/watch?v=d4FvlTzzWjQ