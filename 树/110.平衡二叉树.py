# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_level(root):
            nonlocal balanced
            if not root:
                return 0
            l=get_level(root.left)
            r=get_level(root.right)
            if abs(l-r)>1:
                balanced=False
            return max(l,r)+1

        if not root:
            return True
        balanced=True
        get_level(root)
        return balanced
        
# T：O(n) 计算高度的同时判断是否balanced