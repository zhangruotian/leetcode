from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d:
            return ""
        tv_pairs = self.d[key]
        l,r = 0,len(tv_pairs)
        while l<r:
            m = (l+r-1)//2
            if tv_pairs[m][0]<=timestamp:
                l=m+1
            else:
                r=m
        return tv_pairs[r-1][1] if r-1>=0 else ""
# 相当于找到upper bound，再-1。 注意r=0即使没有比target小的timestamps的时候的处理。
