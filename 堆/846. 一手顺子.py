from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        num_group = len(hand)//groupSize

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        for _ in range(num_group):
            start = min_heap[0]
            for _ in range(groupSize):
                if not start in count or count[start]==0:
                    return False
                count[start]-=1
                if count[start]==0 and start==min_heap[0]:
                    heapq.heappop(min_heap)
                start+=1
        return True
# min heap确定每个group的start value（当前剩余卡的最小值）， dict/counter 查询是否存在构成连续所需要的卡。
# O(nlogn)
