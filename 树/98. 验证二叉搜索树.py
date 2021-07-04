# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left:
            return self.isValidBST(root.right) and self.findMin(root.right) > root.val
        if not root.right:
            return self.isValidBST(root.left) and self.findMax(root.left)<root.val
        if self.isValidBST(root.left) and self.isValidBST(root.right):
            return self.findMax(root.left) < root.val and self.findMin(root.right) > root.val
        return False

    def findMax(self, root):
        if not root:
            return
        while root.right:
            root = root.right
        return root.val

    def findMin(self, root):
        if not root:
            return
        while root.left:
            root = root.left
        return root.val
# 根据定义


class Solution:
    #.  4
    #  3 5
    # 1 2
    def isValidBST(self, root: TreeNode) -> bool:
        self.min_val=float(-inf)
        return self.dfs(root)
    
    def dfs(self,root):
        if not root: return True
        if not self.dfs(root.left):
            return False
        if self.min_val>=root.val:
            return False
        self.min_val=root.val
        return self.dfs(root.right)
#剪枝
# BST中序遍历后是sorted. 