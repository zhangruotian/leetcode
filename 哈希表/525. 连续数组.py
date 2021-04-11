class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #[1,1,0,1,0,0]
        prefix_sum=0
        lookup={0:-1}
        res=0
        for i in range(len(nums)):
            if nums[i]==1:
                prefix_sum+=1
            else:
                prefix_sum-=1
            if prefix_sum not in lookup:
                lookup[prefix_sum]=i
            else:
                res=max(res,i-lookup[prefix_sum])
        return res
#hashmap+prefix sum

#把0变为-1，数量相等则相加=0
#用hashmap记录某个前缀和第一次出现的index i，当这个前缀和再次出现j，说明i-j
#之间和为0，则j-i就是0和1数量相等的子数组的长度

#初始化时记得考虑prefix=0的情况，lookup={0:-1}
#比如[1,1,0,0]如果不初始化{0:-1}，再最后i=3,prefix=0的地方不会得到正确答案

#https://www.youtube.com/watch?v=uAGt1QoAoMU