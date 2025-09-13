class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        last = intervals[0]
        res = 0
        for i in range(1,len(intervals)):
            if last[1]>intervals[i][0]:
                last = [last[0],min(last[1],intervals[i][1])]
                res+=1
            else:
                last = intervals[i]
        return res
        
# 贪心，按前端点排序。往后遍历，如果出现有overlap，保留后端点小的（因为有更小的概率跟再后面的区间发生overlap）。
