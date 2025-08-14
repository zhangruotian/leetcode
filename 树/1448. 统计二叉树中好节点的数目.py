# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        path = []
        self.dfs(root,path)
        return self.res
    
    def dfs(self,root,path):
        if not root:
            return 
        if not path or root.val>=path[-1]:
            self.res+=1
            path.append(root.val)
        else:
            path.append(path[-1])
        self.dfs(root.left,path)
        self.dfs(root.right,path)
        path.pop()

# 类似回溯，用path记录到叶子节点的路径。path中添加的val是到目前为止最大的值，这样就能不管是添加和pop，都能知道到目前为止的最大值。
