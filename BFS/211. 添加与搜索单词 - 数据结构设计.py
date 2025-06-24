class Node:
    def __init__(self):
        self.is_word=False
        self.children={}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        curs = [self.root]
        for c in word:
            new_curs = []
            for cur in curs:
                if c == '.':
                    new_curs+=list(cur.children.values())
                if c in cur.children:
                    new_curs.append(cur.children[c])
            if not new_curs:
                return False
            curs=new_curs

        for cur in curs:
            if cur.is_word:
                return True
        return False
# 208题加强版，用所有词创建trie。208题cur为一个node，本题注意搜索的时候cur可能有很多个node，需要把它们用list中，再往下走。
