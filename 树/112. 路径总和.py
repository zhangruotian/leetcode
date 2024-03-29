# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val==targetSum:
            return True 
        l=self.hasPathSum(root.left,targetSum-root.val)
        if l:
            return True
        r=self.hasPathSum(root.right,targetSum-root.val)
        return r 

#用or简化代码
        
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val==targetSum:
            return True
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)
