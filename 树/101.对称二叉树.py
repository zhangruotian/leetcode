# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricRec(root.left,root.right)
        
    def isSymmetricRec(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val !=right.val:
            return False
        return self.isSymmetricRec(left.left,right.right) and self.isSymmetricRec(left.right,right.left)