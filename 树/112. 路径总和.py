# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root,targetSum)
    
    def dfs(self,root,targetSum):
        if not root:
            return False
        if not root.left and not root.right and targetSum-root.val == 0:
            return True
        left = self.dfs(root.left,targetSum-root.val)
        if left:
            return True
        right = self.dfs(root.right,targetSum-root.val)
        return right
