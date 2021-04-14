# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:return 
        if root.val==key:
            l=root.left
            r=root.right
            if l and r:
                cur=r
                while cur.left:
                    cur=cur.left
                cur.left=l 
                return r
            if l:return l 
            if r:return r
            if not l and not r:return
        if root.val>key:
            root.left=self.deleteNode(root.left,key)  
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        return root
#根据bst规则决定走左还是右
#走到每个node都会返回新的root
#当root.val==key时有四种情况：root有左右，root有左无右，root有右无左，root'=无左右