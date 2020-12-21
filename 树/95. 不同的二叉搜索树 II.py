# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        return self.helper(1,n)

    def helper(self,start,end):
        if start>end:
            return [None]
        tree_list=[]
        for root_val in range(start,end+1):
            left_list=self.helper(start,root_val-1)
            right_list=self.helper(root_val+1,end)
            for l in left_list:
                for r in right_list:
                    root=TreeNode(root_val)
                    root.left=l
                    root.right=r
                    tree_list.append(root)
        return tree_list
        
# 与96题思想一样