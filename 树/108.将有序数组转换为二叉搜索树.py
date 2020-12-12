# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        l=0
        r=len(nums)
        m=(l+r-1)//2
        root=TreeNode(nums[m])
        root.left=self.sortedArrayToBST(nums[l:m])
        root.right=self.sortedArrayToBST(nums[m+1:r])
        return root