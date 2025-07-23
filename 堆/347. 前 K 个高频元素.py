from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)
        t = [(count,num) for num,count in counter.items()]
        min_heap=[]
        for i in range(k):
            heapq.heappush(min_heap,t[i])
        for i in range(k,len(t)):
            heapq.heappushpop(min_heap,t[i])
        for _,num in min_heap:
            res.append(num)
        return res
  # 维护一个element数目为k的min heap，出现次数最小的在最上面。后面只要来的比最顶的大，就heappushandpop，到最后，heap里面就是k个次数最多的。


class MinHeap:
    def __init__(self,data=None,k=0):
        self.data = data
        self.k=k 

    def swapwithsons(self,i):
        min_index = i 
        left = i*2+1
        if left>=self.k:
            return
        if left<self.k and self.data[left][1]<self.data[min_index][1]:
            min_index = left
        right = i*2+2
        if right<self.k and self.data[right][1]<self.data[min_index][1]:
            min_index = right
        self.data[i],self.data[min_index] = self.data[min_index],self.data[i]
        if min_index!=i:
            self.swapwithsons(min_index)
    
    def heapify(self):
        for i in range(self.k-1,-1,-1):
            self.swapwithsons(i)
        
    def pushandpop(self,num):
        self.data[0]=num
        self.swapwithsons(0)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        count = list(count.items())
        min_heap = MinHeap(data=count[:k],k=k)
        min_heap.heapify()
        for i in range(k,len(count)):
            if count[i][1]>min_heap.data[0][1]:
                min_heap.pushandpop(count[i])
        res = []
        for n,c in min_heap.data:
            res.append(n)
        return res

# 自己实现min heap
