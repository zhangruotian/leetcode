class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,5][2,3][4,7]]
        res = 0
        intervals.sort(key=lambda x:x[1])
        i = 0
        while i < len(intervals):
            j = i+1
            while j<len(intervals) and self.overlapping(intervals[i],intervals[j]):
                res+=1
                j+=1
            i = j
        return res
    
    def overlapping(self,interval1,interval2):
        if interval2[0]<interval1[1]:
            return True
        return False
# https://www.youtube.com/watch?v=x6wREca18nw
# 贪心，按后端点排序。往后遍历，如果出现有overlap，保留后端点小的（因为有更小的概率跟再后面的区间发生overlap）。
