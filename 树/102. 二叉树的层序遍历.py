# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # return self.BFS(root)
        res=[]
        self.DFS(root,0,res)
        return res

    def BFS(self,root):
        if not root: 
            return []
        cur=[]
        res=[]
        cur=[root]
        while cur:
            next=[]
            res.append([])
            for node in cur:
                res[-1].append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            cur=next
        return res
    
    def DFS(self,root,level,res):
        if not root:
            return
        if len(res)<=level:
            res.append([])
        res[level].append(root.val)
        self.DFS(root.left,level+1,res)
        self.DFS(root.right,level+1,res)
        
# BFS DFS 都是T:O(n) S:O(n)