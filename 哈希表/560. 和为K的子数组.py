class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #  1 2 3 -1 -2 3    3
        #0 1 3 6  5  3 6.
        n = len(nums)   
        sums = [0]*n
        sums[0]=nums[0]
        for i in range(1,n):
            sums[i]= sums[i-1]+nums[i]
        d = {0:1}
        res = 0
        for i in range(n):
            if sums[i]-k in d:
                res+=d[sums[i]-k]
            d[sums[i]] = d.get(sums[i],0)+1
        return res

                
