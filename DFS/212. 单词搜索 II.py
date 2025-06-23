class Node:
    def __init__(self):
        self.is_word = False
        self.word = None
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word
    
    def search(self,board,i,j,cur,m,n,res):
        if i<0 or i>=m or j<0 or j>=n:
            return 
        if board[i][j]=='#':
            return
        if cur.is_word:
            res.add(cur.word)
            cur.is_word=False
        tmp = board[i][j]
        board[i][j]='#'
        if i+1<m and board[i+1][j] in cur.children:
            self.search(board,i+1,j,cur.children[board[i+1][j]],m,n,res)
        if i-1>=0 and board[i-1][j] in cur.children:
            self.search(board,i-1,j,cur.children[board[i-1][j]],m,n,res)
        if j+1<n and board[i][j+1] in cur.children:
            self.search(board,i,j+1,cur.children[board[i][j+1]],m,n,res)
        if j-1>=0 and board[i][j-1] in cur.children:
            self.search(board,i,j-1,cur.children[board[i][j-1]],m,n,res)
        board[i][j] = tmp

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        trie = Trie()
        for word in words:
            trie.insert(word)
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    trie.search(board,i,j,trie.root.children[board[i][j]],m,n,res)
        return list(res)

# 用 Trie 把所有单词的前缀挂起来，再从每个格子做 DFS，只往 Trie 里存在的分支走；遇到完整单词就加入结果并标记删除
