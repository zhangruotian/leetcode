class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        res = 0
        acc = 0
        for i in range(len(gas)):
            acc+=gas[i]-cost[i]
            if acc<0:
                res = i+1
                acc = 0
        return res
#笔记
