# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_level(root):
            nonlocal balanced
            if not root:
                return 0
            l=get_level(root.left)
            r=get_level(root.right)
            if abs(l-r)>1:
                balanced=False
            return max(l,r)+1

        if not root:
            return True
        balanced=True
        get_level(root)
        return balanced
        
# T：O(n) 计算高度的同时判断是否balanced

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return False if self.getHeight(root)==-1 else True

    def getHeight(self,root):
        if not root:return 0
        l=self.getHeight(root.left)
        if l==-1:return -1
        r=self.getHeight(root.right)
        if r==-1:return -1
        return max(l,r)+1 if abs(l-r)<=1 else -1
# 如果左子树已经返回-1了就不需要再递归右子树了，直接返回-1就可以。<O(N)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:return True
        return  self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.getHeight(root.left)-self.getHeight(root.right))<=1
        
    def getHeight(self,root):
        if not root:return 0
        return max(self.getHeight(root.left),self.getHeight(root.right))+1
# O(n^2) 直接按题意写