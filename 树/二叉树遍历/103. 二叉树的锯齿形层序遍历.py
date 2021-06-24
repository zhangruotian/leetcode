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

#BFS
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res=[]
        cur=[root]
        level=1
        while cur:
            next=[]
            vals=deque()
            for node in cur:
                if level%2==0:
                    vals.appendleft(node.val)
                else:
                    vals.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            cur=next
            level+=1
            res.append(list(vals))
        return res
        