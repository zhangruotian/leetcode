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

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # -2,-2,-2,3,3
        diff = [g-c for g,c in zip(gas,cost)]
        diff_suffix = diff[:]
        for i in range(len(diff_suffix)-2,-1,-1):
            diff_suffix[i] += diff_suffix[i+1]
        start = diff_suffix.index(max(diff_suffix))
        acc = 0
        for i in range(start,len(diff)):
            acc+=diff[i]
            if acc<0:
                return -1
        for i in range(start):
            acc+=diff[i]
            if acc<0:
                return -1
        return start
# 或者用贪心的思想，出发点一定是从它出发能累积最大优势(diff)的点。先确定这个点，然后模拟往下走。
