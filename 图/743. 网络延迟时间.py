import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dists = [float('inf')]*(n+1)
        dists[0] = 0
        dists[k] = 0
        visited = [0]*(n+1)
        min_heap = []
        graph = defaultdict(list)
        for s,e,d in times:
            graph[s].append((d,e))
            if s==k:
                dists[e] = d
                heapq.heappush(min_heap,(d,e))
        while min_heap:
            d,e = heapq.heappop(min_heap)
            if visited[e]:
                continue
            visited[e]=1
            for child_d,child_e in graph[e]:
                if d+child_d<dists[child_e] and not visited[child_e]:
                    dists[child_e] = d+child_d
                    heapq.heappush(min_heap,(dists[child_e],child_e))
        return -1 if max(dists)==float('inf') else max(dists)
      
# single source shortest path to every vertex
# all weights are positive
# Dijkstra algorithm
# https://www.youtube.com/watch?v=XB4MIexjvY0
# 用min heap实现。
