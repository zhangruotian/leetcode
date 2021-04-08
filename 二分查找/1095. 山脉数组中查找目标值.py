# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak_index=self.findPeakIndex(mountain_arr)
        left_index=self.findInLeftOrRight(mountain_arr,peak_index,target,0,peak_index,1)
        if left_index != -1:
            return left_index
        right_index=self.findInLeftOrRight(mountain_arr,peak_index,target,peak_index,mountain_arr.length(),-1)
        return right_index if right_index!=-1 else -1
        
    def findPeakIndex(self,mountain_arr):
        l,r=0,mountain_arr.length()-1
        while l<r:
            m=(l+r-1)//2
            if mountain_arr.get(m)<mountain_arr.get(m+1):
                l=m+1
            if mountain_arr.get(m)>mountain_arr.get(m+1):
                r=m
        return l
    
    def findInLeftOrRight(self,mountain_arr,peak_index,target,left,right,sign):
        l,r=left,right
        while l<r:
            m=(l+r-1)//2
            if mountain_arr.get(m)*sign<target*sign:
                l=m+1
            elif mountain_arr.get(m)*sign>target*sign:
                r=m
            else:
                return m
        return -1 
    
#先二分查找找出峰值对应的index。则左侧单调增，右侧单调减。分别对两侧二分查找
# 使用sign把递增变为递减，精简代码。
#https://www.youtube.com/watch?v=G5IDEoX9bT0
            