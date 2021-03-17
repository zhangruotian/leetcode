# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cnt=0
        return self.dfs(root,k)
    
    def dfs(self,root,k):
        if not root:return
        l=self.dfs(root.left,k)
        if l!=None:return l
        self.cnt+=1
        if self.cnt==k:
            return root.val
        r=self.dfs(root.right,k)
        if r!=None:return r

#找到后停止递归，return
#注意有的test case return的结果是0，因此不能写if l:  而是if l!=None.