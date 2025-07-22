class Solution:
    def build_trie(self,d,word):
        cur = d
        for c in word:
            if not c in cur:
                cur[c] = {}
            cur = cur[c]
        cur['is_word'] = word
    
    def dfs(self,board,i,j,cur,res,m,n,visited):
        if 'is_word' in cur:
            res.add(cur['is_word'])
        if i<0 or i>=m or j<0 or j>=n:
            return
        if visited[i][j]:
            return 
        if board[i][j] not in cur:
            return
        visited[i][j] = 1
        self.dfs(board,i+1,j,cur[board[i][j]],res,m,n,visited)
        self.dfs(board,i-1,j,cur[board[i][j]],res,m,n,visited)
        self.dfs(board,i,j+1,cur[board[i][j]],res,m,n,visited)
        self.dfs(board,i,j-1,cur[board[i][j]],res,m,n,visited)
        visited[i][j] = 0

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d = {}
        res = set()
        m,n = len(board),len(board[0])
        visited = [[0]*n for _ in range(m)]
        for word in words:
            self.build_trie(d,word)
        for i in range(m):
            for j in range(n):
                if board[i][j] in d:
                    self.dfs(board,i,j,d,res,m,n,visited)
        return list(res)


# 用 Trie 把所有单词的前缀挂起来，再从每个格子做 DFS，只往 Trie 里存在的分支走；遇到完整单词就加入结果并标记删除
