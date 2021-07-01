# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# 层序遍历 循环
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return 
        cur=[root]
        while cur:
            next=[]
            for node in cur:
                l=node.left
                r=node.right
                node.left=r
                node.right=l
                if r: 
                    next.append(r)
                if l:
                    next.append(l)
            cur=next
        return root