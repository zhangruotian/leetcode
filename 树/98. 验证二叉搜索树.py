# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        return False if self.dfs(root)==-1 else True
    
    def dfs(self, root):
        if not root:
            return 
        if self.dfs(root.left) == -1:
            return -1
        if root.val<=self.prev:
            return -1
        else:
            self.prev = root.val
        return self.dfs(root.right)
#剪枝 左边不符合的话，右边不用看了
# BST中序遍历后是sorted. 

#iteration
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        stack = []
        self.find_leftmost(root,stack)
        while stack:
            pop = stack.pop()
            if pop.val<=prev:
                return False
            else:
                prev = pop.val
            if pop.right:
                self.find_leftmost(pop.right,stack)
        return True
    
    def find_leftmost(self,node,stack):
        while node:
            stack.append(node)
            node = node.left
