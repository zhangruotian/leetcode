# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        return str(root.val)+' '+l+' '+r

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.pos=-1
        data = data.split(' ')
        return self.deserialize_recur(data)

    def deserialize_recur(self,data):
        self.pos+=1
        if data[self.pos]=='#':
            return None
        root = TreeNode(data[self.pos])
        l = self.deserialize_recur(data)
        r = self.deserialize_recur(data)
        root.left = l
        root.right = r
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
