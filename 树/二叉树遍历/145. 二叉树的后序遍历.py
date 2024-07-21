# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
# recursive

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        self.dfs(root,res)
        return res
    
    def dfs(self,root,res):
        if not root:return
        self.dfs(root.left,res)
        self.dfs(root.right,res)
        res.append(root.val)
# dfs

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #.   1             1245367   4251637 4526731 
    #. 2.  3
    # 4 5  6 7
    #. 9 8
        res, stack = [], []
        self.find_right_most(root,res,stack)
        while stack:
            pop = stack.pop()
            if pop.left:
                self.find_right_most(pop.left,res,stack)
        return res[::-1]
    
    def find_right_most(self, root, res, stack):
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.right 
# iterative
