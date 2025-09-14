import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        new_queries = [(queries[i],i) for i in range(len(queries))]
        new_queries.sort(key=lambda x:x[0])
        res = [-1]*len(queries)
        min_heap = []
        i=0
        for query,index in new_queries:
            while i<len(intervals) and intervals[i][0]<=query:
                heapq.heappush(min_heap,(intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                i+=1
            while min_heap and min_heap[0][1]<query:
                heapq.heappop(min_heap)
            if min_heap:
                res[index] = min_heap[0][0]
        return res


# 通过排序和最小堆进行高效筛选。在按顺序处理每个查询点 q 时，我们利用最小堆进行双向筛选：
# 筛选“入”：将所有已经开始的区间（即 left <= q）的长度和右端点放入最小堆，作为候选。
# 筛选“出”：检查堆顶，将所有已经结束的区间（即 right < q）从堆顶不断移除。
# 经过这两步筛选后，堆里剩下的就都是能覆盖 q 的有效区间，而堆顶自然就是其中长度最短的那个答案。
