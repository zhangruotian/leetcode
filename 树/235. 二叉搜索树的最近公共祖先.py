# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = []
        path_q = []
        self.bs(root,p,path_p)
        self.bs(root,q,path_q)     
        res = 0
        for i in range(min(len(path_p),len(path_q))):
            if path_p[i].val == path_q[i].val:
                res=i 
        return path_p[res]
    
    def bs(self,root,t,path):
        path.append(root)
        if root.val<t.val:
            self.bs(root.right,t,path)
        if root.val>t.val:
            self.bs(root.left,t,path)
        if root.val==t.val:
            return 
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/solutions/428633/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-26/
