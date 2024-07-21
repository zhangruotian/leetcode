
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
# recursive

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        self.dfs(root,res)
        return res
    
    def dfs(self,root,res):
        if not root:return
        self.dfs(root.left,res)
        res.append(root.val)
        self.dfs(root.right,res)
#dfs

class Solution:
    #.   1             1245367   4251637 4526731 
    #. 2.  3
    # 4 5  6 7
    #. 9 8
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        self.find_left_most(root, stack)
        while stack:
            pop = stack.pop()
            res.append(pop.val)
            if pop.right:
                self.find_left_most(pop.right, stack)
        return res
    
    def find_left_most(self,root,stack):
        while root:
            stack.append(root)
            root = root.left
# iterative
