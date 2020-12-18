# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root=root
        self.queue=collections.deque()
        self.in_order(self.root)

    def next(self) -> int:
        return self.queue.popleft().val
        
    def hasNext(self) -> bool:
        return True if self.queue else False
    
    def in_order(self,root):
        if not root:
            return 
        self.in_order(root.left)
        self.queue.append(root)
        self.in_order(root.right)


# 利用in_order_tranversal 把node顺序添加队列