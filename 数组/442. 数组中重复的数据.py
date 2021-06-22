class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            if nums[abs(num)-1]<0:
                res.append(abs(num))
            else:
                nums[abs(num)-1]*=-1
        return res
# 1<=nums[i]<=N   0<=nums[i]-1<=N-1 因此我们可以把value映射到index。
# 将元素转换成数组的索引并对应的将该处的元素乘以-1；
#若数组索引对应元素的位置本身就是负数，则表示已经对应过一次；在结果列表里增加该索引的正数就行；
#例如[2,1,2]
#当走到第一个2时,[2,-1,2]
#当走到第一个1时,[-2,-1,2]
#当走到第一个2时,发现-1为负数，说明前面已经有个2了，因此把2加入res
#注意value可能是负数，要绝对值。加入结果的时候也要绝对值。