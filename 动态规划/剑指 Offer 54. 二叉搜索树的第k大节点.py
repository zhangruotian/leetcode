# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.count=1
        return self.dfs(root,k)
    
    def dfs(self,root,k):
        if not root: return float(inf)

        r=self.dfs(root.right,k)
        if r!=float(inf):
            return r
        if self.count==k:
            return root.val
        self.count+=1

        l=self.dfs(root.left,k)

        return l
#找最大k，由于不知道总节点个数，因此不能从小到大找
#从大到小找，即把中序遍历顺序改反。right->root->left
#找到之后应该提前return

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k=k 
        self.res=0
        self.dfs(root)
        return self.res
    
    def dfs(self,root):
        if not root:return 
        self.dfs(root.right)
        if self.k==0:
            return 
        self.k-=1
        if self.k==0:
            self.res=root.val
        self.dfs(root.left)
#不return的方法，更优美。