class Node:
    def __init__(self):
        self.children={}
        self.is_word=False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=Node()
            cur=cur.children[c]
        cur.is_word=True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.is_word


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True

#理论https://www.youtube.com/watch?v=pkaooVBexeU
#python实现时，children使用字典
#https://www.youtube.com/watch?v=KX2GdDZPxQA

# 用hashtable嵌套
class Trie:

    def __init__(self):
        self.d={}

    def insert(self, word: str) -> None:
        level = self.d
        for c in word:
            if not c in level:
                level[c] = {}
            level = level[c]
        level['is_word'] = True

    def search(self, word: str) -> bool:
        level = self.d
        for c in word:
            if not c in level:
                return False
            level = level[c]
        return 'is_word' in level 

    def startsWith(self, prefix: str) -> bool:
        level = self.d
        for c in prefix:
            if not c in level:
                return False
            level = level[c]
        return True

