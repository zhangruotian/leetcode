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
        stack=[]
        cur=root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur=cur.left
            else:
                tmp=stack.pop()
                cur=tmp.right
        return res
# iterative