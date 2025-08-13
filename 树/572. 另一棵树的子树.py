# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.isSametree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSametree(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSametree(p.left,q.left) and self.isSametree(p.right,q.right)
# 跟100题same tree有点像，但这个需要在每一个node都判断一下

# dfs的过程中判断是否当前的root是不是和subRoot一样，如果找到一样的了，说明最顶部的root里面包含subRoot。
