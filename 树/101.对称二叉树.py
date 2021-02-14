# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricRec(root.left,root.right)
        
    def isSymmetricRec(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val !=right.val:
            return False
        return self.isSymmetricRec(left.left,right.right) and self.isSymmetricRec(left.right,right.left)
# 递归 两个tree: root1.val=root2.val  root1.left和root2.right对称  root1.right和root2.left对称 

class Solution:
    from collections import deque
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue=deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            pop1=queue.popleft()
            pop2=queue.popleft()
            if not pop1 and not pop2:
                continue
            if not pop1 or not pop2 or pop1.val!=pop2.val:
                return False
            queue.append(pop1.left)
            queue.append(pop2.right)
            queue.append(pop1.right)
            queue.append(pop2.left)
        return True
# 循环  维护一个队列 每次pop2个 添加时pop1.left pop2.right pop1.right pop2.left顺序
