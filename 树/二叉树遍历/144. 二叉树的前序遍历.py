# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
# recursive

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        self.dfs(root,res)
        return res
    def dfs(self,root,res):
        if not root:return
        res.append(root.val)
        self.dfs(root.left,res)
        self.dfs(root.right,res)
# dfs 前序遍历与 dfs访问顺序一致

class Solution:
    #.   1             1245367   4251637 4526731 
    #. 2.  3
    # 4 5  6 7
    #. 9 8
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack = []
        self.find_left_most(root, res, stack)
        while stack:
            pop = stack.pop()
            if pop.right:
                self.find_left_most(pop.right, res, stack)
        return res
    
    def find_left_most(self, root, res, stack):
        while root:
            stack.append(root)
            res.append(root.val)
            root = root.left
# iterative
