class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if int(str(nums[i])+str(nums[j]))<int(str(nums[j])+str(nums[i])):
                    nums[i],nums[j]=nums[j],nums[i]
        res=''
        for num in nums:
            res+=str(num)
        return str(int(res))
        #https://www.youtube.com/watch?v=qEIGhVtZ-sg
        #O(n^2)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        str_nums=[str(i) for i in nums]

        def compare(a,b):
            return 1 if a+b>b+a else -1
        
        str_nums.sort(key=cmp_to_key(compare),reverse=1)
        return str(int("".join(str_nums)))

        #o(nlogn)
# python sort(key= ,reverse=1)
#如果不需要改变排序规则，则用lamda即可。
#比如,list[[1,2],[2,1],[0,3]]用第0th元素排序。list.sort(key=lambda x:x[0])

#如果需要改变排序规则，比如本题。需要functools.com_to_key。定义
#一个比较方程compare,然后list.sort(key=com_to_key(compare))
#定义compare()，返回1或-1.