# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val<cur.val and q.val<cur.val:
                cur = cur.left
            elif p.val>cur.val and q.val>cur.val:
                cur = cur.right
            else:
                break
        return cur

# search的过程中，在前面几个node时，p和q的决策是一致的（都要往左，都要往右）。第一次p和q要分开的时候，就是我们要找的最近公共祖先。
# 这里注意要用elif，以防同一个loop运行两个分支。上面改了cur，下面要用cur的时候cur以及变了。
# 当我们明确要求只能进同一个分支，而且判断的var的值可能提前改变的情况下，一定要用elif。
