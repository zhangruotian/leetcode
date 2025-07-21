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

