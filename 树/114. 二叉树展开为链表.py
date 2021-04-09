# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
         
    def dfs(self,root):
        if not root:return None,None
        if not root.left and not root.right:return root,root
        root_l,leaf_l=self.dfs(root.left)
        root_r,leaf_r=self.dfs(root.right)
        if not root_l and not leaf_l:
            root.right=root_r
            return root,leaf_r
        if not root_r and not leaf_r:
            root.right=root_l
            root.left=None
            return root,leaf_l
        leaf_l.right=root_r
        root.right=root_l
        root.left=None
        return root,leaf_r

#分治
#  root_left,leaf_left=flatten(left)
#  root_right,leaf_right=flatten(right)
#  leaf_left.right=root_right
#  root.right=root_right
#  注意把root.left置为0
#  注意处理左侧或者右侧为none的情况
