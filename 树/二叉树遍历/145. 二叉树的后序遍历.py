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
        stack=[]
        cur=root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur=cur.right
            else:
                tmp=stack.pop()
                cur=tmp.left
        return res[::-1]
# iterative