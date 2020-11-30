class Solution:
    def massage(self, nums: List[int]) -> int:
        a,b=0,0
        for i in range(len(nums)):
            a,b=b,max(nums[i]+a,b)
        return b

# 求最大值，考虑动态规划
# 找转移方程：f(i)=max(arr[i]+f(i-2),f(i-1))   f(i)代表从0到i这个array的最优解(最大值)， 如果选择第i个数，则f(i)=arr[i]+f(i-2)
# 不选 f(i)=f(i-1)
# 用list记录下f(0)f(1)f(2)...f(n),代表从0到i子区间的最优解，return list[last_index]即为解:
 f=[0]*len(nums)
        f[0]=nums[0]
        f[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            A= f[i-2]+nums[i]
            B= f[i-1]
            f[i]=max(A,B)
        return f[len(nums)-1]
# 但是此转移方程与斐波那契数列相似，f(i)只与f(i-1)与f(i-2)有关，因此不需要用list记录所有的f(i)，用两个variable依次交替便可。
# 空间复杂度由O(n)---> O(1)