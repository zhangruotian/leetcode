# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if p is root or q is root:
            return root

        left_ancestor=self.lowestCommonAncestor(root.left,p,q)
        right_ancestor=self.lowestCommonAncestor(root.right,p,q)

        if left_ancestor and right_ancestor:
            return root
        if left_ancestor:
            return left_ancestor
        if right_ancestor:
            return right_ancestor
# 时间复杂度：O(N)O(N)，其中 NN 是二叉树的节点数。二叉树的所有节点有且只会被访问一次，因此时间复杂度为 O(N)O(N)。

# 空间复杂度：O(N)O(N) ，其中 NN 是二叉树的节点数。递归调用的栈深度取决于二叉树的高度，二叉树最坏情况下为一条链，此时高度为 NN，因此空间复杂度为 O(N)O(N)。
