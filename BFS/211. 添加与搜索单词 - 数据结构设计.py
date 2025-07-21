from collections import deque
class WordDictionary:
    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        cur = self.d
        for c in word:
            if not c in cur:
                cur[c] = {}
            cur = cur[c]
        cur['is_word'] = True

    def search(self, word: str) -> bool:
        q = deque()
        q.append(self.d)
        for c in word:
            for _ in range(len(q)):
                popped = q.popleft()
                if c in popped:
                    q.append(popped[c])
                if c =='.':
                    for v in popped.values():
                        if type(v)==dict:
                            q.append(v)
            if not q:
                return False
        for r in q:
            if 'is_word' in r:
                return True
        return False
        
# 208题加强版，用所有词创建trie。208题cur为一个node，本题注意搜索的时候cur可能有很多个node，需要把它们用list中，再往下走。
