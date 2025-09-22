"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        for interval in intervals:
            s,e = interval.start,interval.end
            if min_heap and min_heap[0]<=s:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,e)
        return len(min_heap)

# https://www.youtube.com/watch?v=4MEkBvqE_2Q
