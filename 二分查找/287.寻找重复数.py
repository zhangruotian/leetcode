class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = nums[0],nums[nums[0]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        cur1,cur2 = 0,slow 
        while cur1!=cur2:
            cur1 = nums[cur1]
            cur2 = nums[cur2]
        return cur1
# T:O(n)   S:O(1)
# 求链表入环的第一个值
        
