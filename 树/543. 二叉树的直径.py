# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res=0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.height(root)
        return self.res
    
    def height(self,root):
        if not root:
            return 0
        L =self.height(root.left)
        R =self.height(root.right)
        if L+R>self.res:
            self.res=L+R
        return max(L,R)+1
        
        
# 修改求树高的代码即可。 DFS T:O(n)