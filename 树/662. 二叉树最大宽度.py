# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        nodes = [(root,0)]
        while nodes:
            new_nodes = []
            for node,index in nodes:
                if node.left:
                    new_nodes.append((node.left,2*index+1))
                if node.right:
                    new_nodes.append((node.right,2*index+2))
            res = max(res,nodes[-1][1]-nodes[0][1]+1)
            nodes = new_nodes
        return res
# 层序遍历
# 利用完全二叉树性质(heap)，记录下每个node的index
#虽然树不是完全二叉树，但是可以利用完全二叉树的性质计算每一层节点的位置。
