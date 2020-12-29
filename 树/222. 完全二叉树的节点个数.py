# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        level=self.getLevel(root)
        if level:
            return 2**level-1
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1

    def getLevel(self,root):
        count_left=1
        count_right=1
        if not root:
            return 0
        left=root.left
        right=root.right
        while left:
            count_left+=1
            left=left.left
        while right:
            count_right+=1
            right=right.right
        if left==right:
            return left
        else:
            return 0

# 利用完全二叉树的条件
# T:O(logn*logn)
# S:O(logn)
# https://leetcode-cn.com/problems/count-complete-tree-nodes/solution/222-pu-tong-er-cha-shu-yu-wan-quan-er-cha-shu-qi-2/


            

