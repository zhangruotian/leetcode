class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append([float('inf'),float('inf')])
        intervals.insert(0,[float('-inf'),float('-inf')])
        res = []
        n = len(intervals)
        for i in range(n-1):
            if intervals[i][0]<=newInterval[0]<=intervals[i+1][0]:
                if intervals[i][0]<=newInterval[0]<=intervals[i][1]:
                    res.append(self.merge(newInterval,intervals[i]))
                else:
                    res.append(intervals[i])
                    res.append(newInterval)
                break
            else:
                res.append(intervals[i])
        i+=1
        while i<n:
            if res[-1][0]<=intervals[i][0]<=res[-1][1]:
                res[-1] = self.merge(res[-1],intervals[i])
            else:
                res.append(intervals[i])
            i+=1
        return res[1:-1]
    
    def merge(self,interval1,interval2):
        return [min(interval1[0],interval2[0]), max(interval1[1],interval2[1])]
