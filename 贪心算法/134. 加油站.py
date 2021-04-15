class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost)<0:return -1
        start=0
        cur=0
        for i in range(len(gas)):
            cur=cur+gas[i]-cost[i]
            if cur<0:
                start=i+1
                cur=0
        return start
#笔记