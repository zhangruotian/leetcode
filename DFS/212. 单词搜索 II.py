class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.build_trie(words)
        m,n = len(board),len(board[0])
        res = []
        path = []
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    self.dfs(board,i,j,m,n,trie[board[i][j]],res,path,visited)
        return res
    
    def dfs(self,board,i,j,m,n,cur,res,path,visited):
        if visited[i][j]:
            return
        visited[i][j]=True
        path.append(board[i][j])
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        for gi,gj in directions:
            if 0<=i+gi<m and 0<=j+gj<n and board[i+gi][j+gj] in cur:
                self.dfs(board,i+gi,j+gj,m,n,cur[board[i+gi][j+gj]],res,path,visited)
        if 'is_word' in cur:
            res.append(''.join(path))
            cur.pop('is_word')
        visited[i][j]=False
        path.pop()
    
    def build_trie(self,words):
        d = {}
        for word in words:
            cur = d
            for c in word:
                if c not in cur:
                    cur[c]={}
                cur = cur[c]
            cur['is_word']=True
        return d



# 用 Trie 把所有单词的前缀挂起来，再从每个格子做 DFS，只往 Trie 里存在的分支走；遇到完整单词就加入结果并标记删除
