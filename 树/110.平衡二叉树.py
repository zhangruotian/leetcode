# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.getHeight(root)>=0

    def getHeight(self,root):
        if not root:return 0
        l=self.getHeight(root.left)
        if l==-1:return -1
        r=self.getHeight(root.right)
        if r==-1:return -1
        return max(l,r)+1 if abs(l-r)<=1 else -1
# 最优解
# 如果左子树已经返回-1了就不需要再递归右子树了，直接返回-1就可以。<O(N)
