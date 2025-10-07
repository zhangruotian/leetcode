from collections import Counter,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while max_heap or q:
            if q and q[0][1]==time:
                cnt,_ = q.popleft()
                heapq.heappush(max_heap,cnt)
            if max_heap:
                popped = heapq.heappop(max_heap)
                popped+=1
                if popped<0:
                    q.append((popped,time+n+1))
            time+=1
        return time
# https://www.youtube.com/watch?v=s8p8ukTyA2I
