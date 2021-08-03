# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        from collections import deque
        q=deque()
        q.append((root,0))
        res=0
        while q:
            arr=[]
            for _ in range(len(q)):
                node,index=q.popleft()
                arr.append(index)
                if node.left:
                    q.append((node.left,2*index+1))
                if node.right:
                    q.append((node.right,2*index+2))
            res=max(res,arr[-1]-arr[0]+1)
        return res
# 层序遍历
# 利用完全二叉树性质(heap)，记录下每个node的index
# 每层计算arr[-1]-arr[0]+1，保存max
#虽然树不是完全二叉树，但是可以利用完全二叉树的性质计算每一层节点的位置。