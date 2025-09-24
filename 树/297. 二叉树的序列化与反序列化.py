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

前序遍历 (Pre-order): 根 -> 左 -> 右
特性: 总是先访问根节点。
适合场景:
创建树的副本 (Copying a Tree): 因为可以先创建父节点，然后再递归处理子节点。序列化和反序列化本质上就是一种复制。

中序遍历 (In-order): 左 -> 根 -> 右
特性: 对于二叉搜索树 (Binary Search Tree, BST)，中序遍历会得到一个有序的序列。
适合场景:
BST 排序: 这是它最核心的应用。如果你想按升序打印 BST 中的所有键，用中序遍历就对了。

后序遍历 (Post-order): 左 -> 右 -> 根
特性: 总是最后访问根节点。
适合场景:
删除或释放树 (Deleting a Tree): 你必须先删除（或释放）子节点，才能安全地删除父节点，以避免产生孤立节点或内存泄漏。后序遍历的顺序完美契合这个需求。
