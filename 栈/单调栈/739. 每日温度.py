class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1 2 4 3 2 5
        n=len(temperatures)
        res=[0]*n
        stack=[0]
        for i in range(1,n):
            if temperatures[i]<temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]]<temperatures[i]:
                    tmp=stack.pop()
                    res[tmp]=i-tmp
                stack.append(i)
        return res 

#单调栈
#https://www.youtube.com/watch?v=d4FvlTzzWjQ