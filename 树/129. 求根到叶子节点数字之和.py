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
    def sumNumbers(self, root: TreeNode) -> int:
        q=deque([root])
        res=0
        while q:
            for _ in range(len(q)):
                tmp=q.popleft()
                l=tmp.left
                r=tmp.right
                if not l and not r:
                    res+=tmp.val
                if l:
                    l.val=tmp.val*10+l.val
                    q.append(l)
                if r:
                    r.val=tmp.val*10+r.val
                    q.append(r)
        return res
