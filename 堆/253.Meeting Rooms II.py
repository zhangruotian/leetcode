"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        heapq.heappush(min_heap,intervals[0].end)
        for i in range(1,len(intervals)):
            if intervals[i].start>= min_heap[0]:
                heapq.heapreplace(min_heap,intervals[i].end)
            else:
                heapq.heappush(min_heap,intervals[i].end)
        return len(min_heap)

# https://www.youtube.com/watch?v=4MEkBvqE_2Q
