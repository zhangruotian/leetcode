# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root_val=preorder[0]
        root=TreeNode(root_val)
        if len(preorder) ==1:
            return root
        index=inorder.index(root_val)
        root.left=self.buildTree(preorder[1:1+index],inorder[0:index])
        root.right=self.buildTree(preorder[1+index:],inorder[index+1:])
        return root
 # preorder的第一个是root。在inorder中，root左边的是root.left，右边同理。分治递归即可。


 #followup: 给前序和中序，输出后序
 class Solution:
     def getPostOrder(self,preorder,inorder):
            if not preorder: return []
            root_val=preorder[0]
            index=inorder.index(root_val)
            l=self.getPostOrder(preorder[1:index+1],inorder[:index])
            r=self.getPostOrder(preorder[index+1:],inorder[index+1:])
            return l+r+[root_val]