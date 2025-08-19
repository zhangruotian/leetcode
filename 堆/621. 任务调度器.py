import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-1*c for c in counter.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while max_heap or q:
            if max_heap:
                heap_popped = heapq.heappop(max_heap)
                if heap_popped+1!=0:
                    q.append((heap_popped+1,time+n))
            if q and q[0][1]==time:
                heapq.heappush(max_heap,q.popleft()[0])
            time+=1
        return time
# https://www.youtube.com/watch?v=s8p8ukTyA2I
