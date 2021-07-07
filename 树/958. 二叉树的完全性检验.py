# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def isCompleteTree(self, root: TreeNode) -> bool:
        q=deque()
        q.append(root)
        meet_none=False
        while q:
            for _ in range(len(q)):
                pop=q.popleft()
                left=pop.left
                right=pop.right
                if not left:
                    meet_none=True
                else:
                    if meet_none:
                        return False
                    q.append(left)
                if not right:
                    meet_none=True
                else:
                    if meet_none:
                        return False
                    q.append(right)
        return True
# 利用层序遍历，如果遇到None，标记meet_node=True 后面如果遇到不是None的而且meet_node=True，则不是完备二叉树

#用list代码简单
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        cur=[root]
        hasNone=False
        while cur:
            next=[]
            for node in cur:
                if hasNone and node:
                    return False
                if not node:
                    hasNone=True
                    continue
                next.append(node.left)
                next.append(node.right)
            cur=next
        return True