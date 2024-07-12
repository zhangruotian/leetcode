class Solution:
    #  0
    # 1 2
    #3 4 5
    # left = 2*i+1, right = 2*i+2
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heapify(nums)
        for i in range(len(nums)-1,-1,-1):
            nums[i],nums[0] = nums[0],nums[i]
            self.swap_with_sons(nums,0,i-1)
        return nums[-k]

    
    def swap_with_sons(self,nums,i,r):
        left_index = 2*i+1
        right_index = 2*i+2
        max_index = i
        if left_index<=r and nums[left_index] > nums[max_index]:
            max_index = left_index
        if right_index<=r and nums[right_index] > nums[max_index]:
            max_index = right_index
        if max_index==i:
            return
        nums[max_index], nums[i] = nums[i],nums[max_index]
        self.swap_with_sons(nums,max_index,r)
    
    def heapify(self,nums):
        for i in range(len(nums)-1,-1,-1):
            self.swap_with_sons(nums,i,len(nums)-1)



class Solution:
    #  0
    # 1 2
    #3 4 5
    # left = 2*i+1, right = 2*i+2
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = len(nums)-k
        self.heapify(nums)
        for i in range(len(nums)-1,-1,-1):
            nums[i],nums[0] = nums[0],nums[i]
            if i ==pos:
                return nums[i]
            self.swap_with_sons(nums,0,i-1)

    def swap_with_sons(self,nums,i,r):
        left_index = 2*i+1
        right_index = 2*i+2
        max_index = i
        if left_index<=r and nums[left_index] > nums[max_index]:
            max_index = left_index
        if right_index<=r and nums[right_index] > nums[max_index]:
            max_index = right_index
        if max_index==i:
            return
        nums[max_index], nums[i] = nums[i],nums[max_index]
        self.swap_with_sons(nums,max_index,r)
    
    def heapify(self,nums):
        for i in range(len(nums)-1,-1,-1):
            self.swap_with_sons(nums,i,len(nums)-1)

# 找到倒数第k个停止
