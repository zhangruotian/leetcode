
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                tmp=stack.pop()
                res.append(tmp.val)
                root=tmp.right
        return res
# iterative
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/        

# 中序 前序 后序 层序 遍历，dfs和iterative模板: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/python3-er-cha-shu-suo-you-bian-li-mo-ban-ji-zhi-s/

#新代码
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = []
        res = []
        self.left_most(root,stack)
        while stack:
            pop = stack.pop()
            res.append(pop.val)
            if pop.right:
                self.left_most(pop.right, stack)
        return res
    
    def left_most(self,root,stack):
        while root:
            stack.append(root)
            root = root.left
