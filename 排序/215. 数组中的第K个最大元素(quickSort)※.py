class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.quickSort(nums,0,len(nums)-1)
        return nums[-k]

    def partition(self,nums,start,end):
        pi=start
        s=start+1
        e=end
        while True:
            while s<e and nums[s]<nums[pi]:   #while s<=end and nums[s]<=pivot:
                s+=1
            while s<=e and nums[e]>=nums[pi]:  #while e>0 and nums[e]>pivot:
                e-=1
            if s<e:
                nums[s],nums[e]=nums[e],nums[s]
            else:
                break
        nums[e],nums[pi]=nums[pi],nums[e]
        return e

    def quickSort(self,nums,start,end):
        if start>=end:
            return                            
        mid=self.partition(nums, start, end)
        self.quickSort(nums, 0, mid-1)
        self.quickSort(nums, mid+1, end)
# 快排 nlogn
# 递归深度logn，每层把pivot放中间 n。时间复杂度 O(nlogn)。最差情况 ：已排序。时间复杂度O(n2)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res_index=len(nums)-k
        return self.quickSort(nums,0,len(nums)-1,res_index)

    def partition(self,nums,start,end):
        pi=start
        s=start+1
        e=end
        while True:
            while s<e and nums[s]<nums[pi]:
                s+=1
            while s<=e and nums[e]>=nums[pi]:
                e-=1
            if s<e:
                nums[s],nums[e]=nums[e],nums[s]
            else:
                break
        nums[e],nums[pi]=nums[pi],nums[e]
        return e

    def quickSort(self,nums,start,end,res_index):              
        mid=self.partition(nums, start, end)
        if mid == res_index:
            return nums[mid]
        if mid > res_index:
            return self.quickSort(nums, 0, mid-1,res_index)
        if mid < res_index:
            return self.quickSort(nums, mid+1, end,res_index)
#每次经过「划分」操作后，我们一定可以确定一个元素的最终位置，即 x 的最终位置为 q，并且保证 a[l⋯q−1] 中的每个元素小于等于 a[q]，且 a[q] 小于等于a[q+1⋯r] 中的每个元素。
#所以只要某次划分的 q 为倒数第 k 个下标的时候，我们就已经找到了答案。 
#我们只关心这一点，a[l⋯q−1] 和a[q+1⋯r] 是否是有序的，我们不关心。

class Solution:
    from random import randint
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res_index=len(nums)-k
        return self.quickSort(nums,0,len(nums)-1,res_index)

    def partition(self,nums,start,end):
        pi=start
        s=start+1
        e=end
        while True:
            while s<e and nums[s]<nums[pi]:
                s+=1
            while s<=e and nums[e]>=nums[pi]:
                e-=1
            if s<e:
                nums[s],nums[e]=nums[e],nums[s]
            else:
                break
        nums[e],nums[pi]=nums[pi],nums[e]
        return e
    
    def randomPartition(self,nums,start,end):
        r=randint(start,end)
        nums[r],nums[end]=nums[end],nums[r]
        return self.partition(nums,start,end)

    def quickSort(self,nums,start,end,res_index):              
        mid=self.randomPartition(nums, start, end)
        if mid == res_index:
            return nums[mid]
        if mid > res_index:
            return self.quickSort(nums, 0, mid-1,res_index)
        if mid < res_index:
            return self.quickSort(nums, mid+1, end,res_index)
# 我们知道快速排序的性能和「划分」出的子数组的长度密切相关。
# 直观地理解如果每次规模为 n 的问题我们都划分成 1和 n - 1，每次递归的时候又向 n - 1 的集合中递归，这种情况是最坏的，
# 时间代价是 O(n ^ 2)。我们引入随机化加速这一过程。
# 运行时间由1600ms变为200ms。



#另外两种partition写法

#以end为pivot，最简单代码
def partition(self,nums,start,end):
    pivot=nums[end]
    pIndex=start
    for i in range(start,end):
        if nums[i]<pivot:
            nums[i],nums[pIndex]=nums[pIndex],nums[i]
            pIndex+=1
    nums[end],nums[pIndex]=nums[pIndex],nums[end]
    return pIndex

#以start为pivot，用在链表的快排
def partition(self,nums,start,end):
        pivot=nums[start]
        pIndex=start+1
        for i in range(start+1,end+1):
            if nums[i]<pivot:
                nums[i],nums[pIndex]=nums[pIndex],nums[i]
                pIndex+=1
        nums[start],nums[pIndex-1]=nums[pIndex-1],nums[start]
        return pIndex-1


