"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:return
        self.head=None
        self.prev=None
        self.dfs(root)
        self.head.left=self.prev
        self.prev.right=self.head
        return self.head
    
    def dfs(self,root):
        if not root:return
        self.dfs(root.left)
        if not self.prev:
            self.head=root
        else:
            self.prev.right=root
            root.left=self.prev
        self.prev=root
        self.dfs(root.right)
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
#利用全局变量记录状态
a=True
def abc(a):
	a=False
abc(a)
print(a)
#传参不可以，相当与a=True b=a b=False a不会变
a=True
def abc(a):
	print(a)
abc(a)
# 可以打印，a是全局变量，但是如果想改变a的数，需要global
a=True
def abc():
	global a
    a=False
abc()
print(a)
# 此时a已经改变
class Test:
    a=True
    def abc():
        global a
        a=False
#类内可以用全局变量记录状态
class Test:
    def __init__(self):
        self.a=True
    def abc():
        self.a=False
#用self记录

        

