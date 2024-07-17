# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.dfs(root, res, 0)
        return [list(r) for r in res]
        
    
    def dfs(self, root, res, level):
        if not root: return 
        if len(res)<level+1:
            res.append(deque())
        if level%2 == 0:
            res[level].append(root.val)
        else:
            res[level].appendleft(root.val)
        self.dfs(root.left,res,level+1)
        self.dfs(root.right,res,level+1)


#BFS
class Solution:
    from collections import deque
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        nodes = [root]
        res = []
        left_to_right = True
        while nodes:
            level_res = deque()
            new_nodes = []
            for node in nodes:
                if left_to_right:
                    level_res.append(node.val)
                else:
                    level_res.appendleft(node.val)
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            nodes = new_nodes 
            res.append(list(level_res))
            left_to_right = not left_to_right
        return res
        
