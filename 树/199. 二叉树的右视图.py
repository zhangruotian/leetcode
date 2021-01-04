# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res=[]
        self.DFS(root,0,res)
        return res

    def DFS(self,root,level,res):
        if not root:
            return
        if len(res)<=level:
            res.append(0)
        res[level]=root.val
        self.DFS(root.left,level+1,res)
        self.DFS(root.right,level+1,res)
# 与102相同 层序遍历找最后元素