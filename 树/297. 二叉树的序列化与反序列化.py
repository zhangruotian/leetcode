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
        serialized=[]
        self.serialize_recur(root,serialized)
        return ' '.join(serialized)

    def serialize_recur(self,root,serialized):
        if not root:
            serialized.append('#')
            return
        serialized.append(str(root.val))
        self.serialize_recur(root.left,serialized)
        self.serialize_recur(root.right,serialized)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        serialized = data.split(' ')
        self.pos=0
        return self.deserialize_recur(serialized)
    
    def deserialize_recur(self,serialized):
        # 11 12 # # 13 # #
        cur = serialized[self.pos]
        self.pos+=1
        if cur =='#':
            return None
        node = TreeNode(int(cur))
        node.left=self.deserialize_recur(serialized)
        node.right=self.deserialize_recur(serialized)
        return node
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
