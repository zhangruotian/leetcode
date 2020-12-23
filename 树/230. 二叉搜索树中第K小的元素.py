# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count=0
    res=float('-inf')
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.in_order_traversal(root,k)
        return self.res
    
    def in_order_traversal(self,root,k):
        if not root:
            return
        self.in_order_traversal(root.left,k)
        self.count+=1
        if self.count==k:
            self.res=root.val
        elif self.count>k:
            return
        self.in_order_traversal(root.right,k)

# 中序遍历+剪枝