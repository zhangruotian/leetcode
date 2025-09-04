class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indices = {}
        n = len(s)
        for i in range(n):
            last_indices[s[i]]=i
        res = []
        start = 0
        while start<n:
            end = last_indices[s[start]]
            i = start
            while i<=end:
                if last_indices[s[i]]>end:
                    end = last_indices[s[i]]
                i+=1
            res.append(end+1-start)
            start = end+1
        return res
# 从start开始，一直到end，尝试更新end，一直到把重复字母都覆盖在end里面。再从新的start开始。
