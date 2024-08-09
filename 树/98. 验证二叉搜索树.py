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
