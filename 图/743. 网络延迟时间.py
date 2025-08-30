import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s,e,t in times:
            graph[s].append((e,t))

        res = [float('inf')]*(n+1)
        res[k] = 0
        min_heap = [(0,k)]
        visited = [0]*(n+1)
        while sum(visited)<n:
            if not min_heap:
                return -1
            cdist,node = heapq.heappop(min_heap)
            if cdist<res[node]:
                continue
            visited[node]=1
            for child,edge in graph[node]:
                if visited[child]:
                    continue
                if cdist+edge<res[child]:
                    res[child] = cdist+edge
                    heapq.heappush(min_heap,(cdist+edge,child))
        longest = max(res[1:])
        return -1 if longest==float('inf') else longest
      
# single source shortest path to every vertex
# all weights are positive
# Dijkstra algorithm
# https://www.youtube.com/watch?v=XB4MIexjvY0
# 用min heap实现。
