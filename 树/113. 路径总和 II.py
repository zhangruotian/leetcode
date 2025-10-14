# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path,res = [],[]
        self.dfs(root,path,res,targetSum)
        return res
    
    def dfs(self,root,path,res,target):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and root.val==target:
            res.append(path[:])
        self.dfs(root.left,path,res,target-root.val)
        self.dfs(root.right,path,res,target-root.val)
        path.pop()
