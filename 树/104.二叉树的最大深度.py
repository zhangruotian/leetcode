# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        return max(l,r)+1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nodes = [root]
        level = 0
        while nodes:
            level+=1
            new_nodes = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            nodes = new_nodes
        return level
