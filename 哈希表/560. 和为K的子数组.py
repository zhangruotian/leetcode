class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map={0:1}
        cum_sum=0
        res=0
        for num in nums:
            cum_sum+=num
            if cum_sum-k in sum_map:
                res+=sum_map[cum_sum-k]
            if cum_sum in sum_map:
                sum_map[cum_sum]+=1
            else:
                sum_map[cum_sum]=1
        return res


