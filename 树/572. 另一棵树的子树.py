# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSame(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
         
    def isSame(self,root1,root2):
        if not root1 and not root2:
            return True
        if root1 and not root2:
            return False
        if root2 and not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.isSame(root1.left,root2.left) and self.isSame(root1.right,root2.right)

# dfs的过程中判断是否当前的root是不是和subRoot一样，如果找到一样的了，说明最顶部的root里面包含subRoot。
