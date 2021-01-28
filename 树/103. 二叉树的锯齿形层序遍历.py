# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        self.dfs(root,res,0)
        return res
    
    def dfs(self,root,res,level):
        if not root:
            return
        if len(res)<=level:
            res.append([])
        if level%2==0:
            res[level].append(root.val)
        else:
            res[level].insert(0,root.val)
        self.dfs(root.left,res,level+1)
        self.dfs(root.right,res,level+1)
        