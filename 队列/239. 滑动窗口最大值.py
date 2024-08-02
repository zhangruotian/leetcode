#单调队列
#https://www.youtube.com/watch?v=2SXqBsTR6a8
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
