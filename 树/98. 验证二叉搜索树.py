# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #.  4
    #  3 5
    # 1 2
    def isValidBST(self, root: TreeNode) -> bool:
        self.min_val=float(-inf)
        return self.dfs(root)
    
    def dfs(self,root):
        if not root: return True
        if not self.dfs(root.left):
            return False
        if self.min_val>=root.val:
            return False
        self.min_val=root.val
        return self.dfs(root.right)
#剪枝
# BST中序遍历后是sorted. 

#iteration
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        max_val=float(-inf)
        stack=[]
        cur=root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                tmp=stack.pop()
                if tmp.val<=max_val:
                    return False
                max_val=tmp.val
                cur=tmp.right
        return True 