class Solution:
    def merge(self, intervals) :
        intervals.sort(key= lambda x:x[0])
        merged=[]
        for i in intervals:
            if not merged or i[0]>merged[-1][1]:
                merged.append(i)
            else:
                if i[1]>merged[-1][1]:
                    merged[-1]=[merged[-1][0],i[1]]
        return merged

# 根据第一个元素排序。
# 时间复杂度O(nlogn)