class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_index = 0
        starts=[0]+list(map(lambda x:x[0],intervals))+[float('inf')]
        for i in range(1,len(starts)):
            if starts[i-1]<=newInterval[0]<=starts[i]:
                insert_index = i-1
        intervals.insert(insert_index,newInterval)
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                res[-1] = [res[-1][0],max(res[-1][1],intervals[i][1])]
            else:
                res.append(intervals[i])
        return res
                
        
            

