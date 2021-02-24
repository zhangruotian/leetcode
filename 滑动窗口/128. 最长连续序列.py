class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        hashtable={}
        for num in nums:
            if num in hashtable:
                continue
            left=num-1 in hashtable
            right=num+1 in hashtable
            if not left and not right:
                hashtable[num]=1
            if left and right:
                l=hashtable[num-1]
                r=hashtable[num+1]
                hashtable[num-l]=l+r+1
                hashtable[num+r]=l+r+1
                hashtable[num]=1
            if left and not right:
                l=hashtable[num-1]
                hashtable[num]=l+1
                hashtable[num-l]=l+1
            if right and not left:
                r=hashtable[num+1]
                hashtable[num]=r+1
                hashtable[num+r]=r+1
        print(hashtable)
        return max(hashtable.values())
# https://www.youtube.com/watch?v=rc2QdQ7U78I

# 首先跳过重复元素，否则会导致结果出错
# hashtable={num : 以该num为边界的连续数组的长度}
# [1 2 3] hashmap={1:2,2:2} 要加入3 则找a=hashtable[3-1]，a+1即hashtable[3]的value。同时更新hashmap[3-2]
# 向左侧延续同理
# 如果既没有num-1也没有num+1.则hashmap[num]=1
# 如果都有，则为桥梁，hashtable[num-l]=l+r+1 hashtable[num+r]=l+r+1 hashtable[num]=1(这个不能忘，随便取值都行。如果不写，则相当于没跳过重复元素，会出错)
# T:o(n) S:o(n)

