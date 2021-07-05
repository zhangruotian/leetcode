class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for i in range(k):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        
        for i in range(k,len(nums)):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            while q and i-q[0]>=k:
                q.popleft()
            res.append(nums[q[0]])
        return res

#单调队列
#https://www.youtube.com/watch?v=2SXqBsTR6a8
#https://labuladong.github.io/algo/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E5%8D%95%E8%B0%83%E9%98%9F%E5%88%97.html

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for i in range(len(nums)):
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            if i-q[0]==k:
                q.popleft()
            if i>=k-1:
                res.append(nums[q[0]])
        return res