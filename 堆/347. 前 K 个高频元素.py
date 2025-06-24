class Solution:
    import heapq
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = tuple(Counter(nums).items())
        min_heap = []
        i = 0
        while len(min_heap)<k:
            heapq.heappush(min_heap,(count[i][1],count[i][0]))
            i+=1
        while i<len(count):
            if count[i][1]>min_heap[0][0]:
                heapq.heappushpop(min_heap,(count[i][1],count[i][0]))
            i+=1
        res = []
        for c,n in min_heap:
            res.append(n)
        return res
  # 维护一个element数目为k的min heap，出现次数最小的在最上面。后面只要来的比最顶的大，就heappushandpop，到最后，heap里面就是k个次数最多的。
