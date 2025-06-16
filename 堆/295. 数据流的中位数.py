class MedianFinder:
    # max:
    #  3 
    # 2 1

    # min:
    #  4 
    # 5 
    import heapq  
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if len(self.maxheap)==len(self.minheap):
            heapq.heappush(self.maxheap,-heapq.heappushpop(self.minheap,num))
        else:
            heapq.heappush(self.minheap,-heapq.heappushpop(self.maxheap,-num))

    def findMedian(self) -> float:
        if len(self.maxheap)==len(self.minheap):
            return (-self.maxheap[0]+self.minheap[0])/2
        else:
            return -self.maxheap[0]
# https://leetcode.cn/problems/find-median-from-data-stream/solutions/3015873/ru-he-zi-ran-yin-ru-da-xiao-dui-jian-ji-4v22k/
