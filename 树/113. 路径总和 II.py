# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [],[]
        self.dfs(root,res,path,targetSum)
        return res
    
    def dfs(self,root,res,path,targetSum):
        if not root:
            return 
            
        path.append(root.val)
        if sum(path) == targetSum and not root.left and not root.right:
            res.append(path[:])
        self.dfs(root.left,res,path,targetSum)
        self.dfs(root.right,res,path,targetSum)
        path.pop()

# 使用path记录，dfs递归过程中不产生额外的内存


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if root.val != sum:
                return []
            else:
                return [[root.val]]
        res=[]
        
        l=self.pathSum(root.left,sum-root.val)
        res+=[[root.val]+i for i in l]
        
        r=self.pathSum(root.right,sum-root.val)
        res+=[[root.val]+i for i in r]
    
        return res
# 内存占用多
