# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.res=False
        self.dfs(root,targetSum)
        return self.res

    def dfs(self,root,target):

        if not root:return
        print(root.val)
        if root.val==target and (not root.left and not root.right):
            self.res=True
            return 
        self.dfs(root.left,target-root.val)
        if self.res:return 
        self.dfs(root.right,target-root.val)
        if self.res:return 
