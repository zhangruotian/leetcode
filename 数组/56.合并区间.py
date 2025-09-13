class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                res[-1] = [res[-1][0],max(res[-1][1],intervals[i][1])]
            else:
                res.append(intervals[i])
        return res
# 根据第一个元素排序。
# 时间复杂度O(nlogn)
