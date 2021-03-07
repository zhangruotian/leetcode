# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k=k
        return self.dfs(root)
    
    def dfs(self,root):
        if not root:return 
        r=self.dfs(root.right)
        if r:return r
        self.k-=1
        if self.k==0:
            return root.val
        l=self.dfs(root.left)
        if l:return l 
#找最大k，由于不知道总节点个数，因此不能从小到大找
#从大到小找，即把中序遍历顺序改反。right->root->left
#找到之后应该提前return