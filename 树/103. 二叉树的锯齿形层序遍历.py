# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        self.DFS(root,0,res)
        for index,list in enumerate(res):
            if index %2!=0:
                res[index]=res[index][::-1]
        return res


    def DFS(self,root,level,res):
        if not root:
            return
        if len(res)<=level:
            res.append([])

        res[level].append(root.val)

        self.DFS(root.left,level+1,res)
        self.DFS(root.right,level+1,res)
# 与102相同