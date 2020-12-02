class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
        return res
# 首先对数组进行排序，排序后固定一个数 nums[i]，再使用左右指针指向 nums[i]后面的两端，数字分别为 nums[L] 和 nums[R]，
# 如果 nums[i]大于 0，则三数之和必然无法等于 0，结束循环
# 如果 nums[i] == nums[i-1]，则说明该数字重复，会导致结果重复，所以应该跳过 
# 计算三个数的和 sum 判断是否满足为 00，满足则添加进结果集
# 1. 当 sum == 0 时，nums[L] == nums[L+1] 则会导致结果重复，应该跳过，L++
# 2. 当 sum == 0 时，nums[R] == nums[R-1] 则会导致结果重复，应该跳过，R--
# 当 sum<0时，L++
# 当 sum>0时，R--

