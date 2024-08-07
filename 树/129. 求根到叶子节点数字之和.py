# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res=0
        self.dfs(root)
        return self.res

    def dfs(self,root):
        if not root:
            return
        if not root.left and not root.right:
            self.res+=root.val
        if root.left:
            root.left.val=root.val*10+root.left.val
        if root.right:
            root.right.val=root.val*10+root.right.val 
        self.dfs(root.left)
        self.dfs(root.right)
# 二叉树的每条从根节点到叶子节点的路径都代表一个数字。
#其实，每个节点都对应一个数字，等于其父节点对应的数字乘以 1010 再加上该节点的值（这里假设根节点的父节点对应的数字是 00）。
#只要计算出每个叶子节点对应的数字，然后计算所有叶子节点对应的数字之和，即可得到结果。


#bfs循环
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        nodes = [root]
        while nodes:
            new_nodes = []
            for node in nodes:
                if not node.left and not node.right:
                    res+=node.val
                if node.left:
                    node.left.val = node.val*10+node.left.val
                    new_nodes.append(node.left)
                if node.right:
                    node.right.val = node.val*10+node.right.val
                    new_nodes.append(node.right)
            nodes = new_nodes
        return res
