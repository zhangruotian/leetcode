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
        res=[]
        self.dfsSerialize(root,res)
        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=data.split(" ")
        self.pos=-1
        return self.dfsDeserialize(data)
    
    def dfsSerialize(self,root,res):
        if not root:
            res.append("#")
            return 
        res.append(str(root.val))
        self.dfsSerialize(root.left,res)
        self.dfsSerialize(root.right,res)
    
    def dfsDeserialize(self,data):
        self.pos+=1
        if data[self.pos]=="#":
            return
        root=TreeNode(int(data[self.pos])) 
        root.left=self.dfsDeserialize(data)
        root.right=self.dfsDeserialize(data)
        return root

# https://www.youtube.com/watch?v=JL4OjKV_pGE