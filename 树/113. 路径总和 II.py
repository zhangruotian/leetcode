# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res=[]
        path=[]
        self.dfs(root,sum,path,res)
        return res
    
    def dfs(self,root,sum,path,res):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            if root.val==sum:
                res.append(path[:])
        
        self.dfs(root.left,sum-root.val,path,res)
        self.dfs(root.right,sum-root.val,path,res)
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