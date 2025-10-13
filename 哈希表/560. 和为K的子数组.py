from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]*(n+1)
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1]+nums[i-1]
        res = 0
        count = Counter()
        for i in range(n+1):
            res+=count[prefix_sum[i]-k]
            count[prefix_sum[i]]+=1
        return res
# prefix sum + hashmap 
# 跟two sum那题一样，只不过是减法


  

                
