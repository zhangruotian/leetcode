from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize!=0:
            return False
        counter = Counter(hand)
        min_heap = list(counter.keys())
        heapq.heapify(min_heap)
        for _ in range(n//groupSize):
            while counter[min_heap[0]]==0:
                heapq.heappop(min_heap)
            start = min_heap[0]
            for i in range(groupSize):
                if counter[i+start]==0:
                    return False
                counter[start+i]-=1
        return True
# min heap确定每个group的start value（当前剩余卡的最小值）， dict/counter 查询是否存在构成连续所需要的卡。
# O(nlogn)
