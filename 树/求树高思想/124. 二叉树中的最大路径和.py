# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res=float(-inf)
    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.res

    def helper(self,root):
        if not root:
            return 0
        l=self.helper(root.left)
        r=self.helper(root.right)
        self.res=max((root.val+max(l,0)+max(r,0)),self.res)
        return max(l,r,0)+root.val
# 与543相似 O(n) O(H)