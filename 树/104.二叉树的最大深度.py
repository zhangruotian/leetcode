# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            depth_left=self.maxDepth(root.left)+1
            depth_right=self.maxDepth(root.right)+1
            return max(depth_left,depth_right)