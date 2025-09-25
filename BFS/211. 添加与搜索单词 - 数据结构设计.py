class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        cur = self.d
        for c in word:
            if c not in cur:
                cur[c]={}
            cur = cur[c]
        cur['is_word']=True

    def search(self, word: str) -> bool:
        curs = [self.d]
        for c in word:
            new_curs = []
            for cur in curs:
                if c in cur:
                    new_curs.append(cur[c])
                elif c=='.':
                    for key,next in cur.items():
                        if not key=='is_word':
                            new_curs.append(next)
            if not new_curs:
                return False
            curs = new_curs
        for cur in curs:
            if 'is_word' in cur:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
        
# 208题加强版，用所有词创建trie。208题cur为一个node，本题注意搜索的时候cur可能有很多个node，需要把它们用list中，再往下走。
