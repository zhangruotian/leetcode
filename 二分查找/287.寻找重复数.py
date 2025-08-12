class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=1
        r=len(nums)+1
        while l<r:
            m=(l+r-1)//2
            count=0
            for num in nums:
                if num<=m:
                    count+=1
            if count>m:
                r=m
            else:
                l=m+1
        return l
        
# T:O(nlogn)   S:O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = nums[0],nums[nums[0]]
        while True:
            if slow==fast:
                break
            slow = nums[slow]
            fast = nums[nums[fast]]
        cur2 = nums[slow]
        cur1 = nums[0]
        while True:
            if cur1==cur2:
                return cur1
            cur1 = nums[cur1]
            cur2 = nums[cur2]
# T:O(n)   S:O(1)
# 求链表入环的第一个值
        
