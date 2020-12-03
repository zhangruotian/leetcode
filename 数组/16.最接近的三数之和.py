class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length=len(nums)
        res= nums[0]+nums[1]+nums[length-1]
        distance=abs(target-res)
        for i in range(length-2):
            l=i+1
            r=length-1
            while l<r:
                three_sum=nums[i]+nums[l]+nums[r]
                if abs(target-three_sum)<distance:
                    distance=abs(target-three_sum)
                    res= three_sum
                if three_sum==target:
                    return target
                elif three_sum<target:
                    l+=1
                else:
                    r-=1
        return res
        
# 双指针
# 注意判断与target的距离时用绝对值。target=10, a=1,b=2 ,target-b<target-a, 因此b更接近target。target=-10, target-b<target-a, 但是实际a与target更接近。
# distance=abs(target-x)
