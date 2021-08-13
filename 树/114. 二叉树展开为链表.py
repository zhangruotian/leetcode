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
        self.prev=None
        self.dfs(root)
    
    def dfs(self,root):
        if not root: return 
        l=root.left
        r=root.right
        if self.prev:
            self.prev.left=None
            self.prev.right=root
        self.prev=root
        self.dfs(l)
        self.dfs(r)

# 用prev记录前面的节点，prev.left=None prev.right=root
# 改变了prev的右节点，导致dfs无法正确遍历，因此用l=root.left  r=root.right先记录下来
