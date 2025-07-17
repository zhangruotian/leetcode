class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==1:
            return 0
        intervals.sort(key=lambda x:x[1])
        i,j = 0,1
        res = 0
        while j<len(intervals):
            if intervals[j][0]<intervals[i][1]:
                res+=1
                j+=1
            else:
                i=j
                j+=1
        return res
        
# https://www.youtube.com/watch?v=x6wREca18nw
# 贪心，按后端点排序。往后遍历，如果出现有overlap，保留后端点小的（因为有更小的概率跟再后面的区间发生overlap）。
