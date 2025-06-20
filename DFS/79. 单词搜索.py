class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board,word,i,j,0,m,n):
                    return True
        return False
    
    def dfs(self,board,word,i,j,pos,m,n):
        if i<0 or i>=m:
            return False
        if j<0 or j>=n:
            return False
        if board[i][j] == '#':
            return False
        if board[i][j]!=word[pos]:
            return False
        if board[i][j]==word[pos] and pos==len(word)-1:
            return True
        tmp=board[i][j] 
        board[i][j] = '#'
        l = self.dfs(board,word,i,j-1,pos+1,m,n)
        r = self.dfs(board,word,i,j+1,pos+1,m,n)
        t = self.dfs(board,word,i-1,j,pos+1,m,n)
        b = self.dfs(board,word,i+1,j,pos+1,m,n)
        board[i][j] = tmp
        return l or r or t or b
# 主逻辑（exist 方法）：
# 遍历整个网格，每个点作为起点尝试搜索 word。
# 如果某个起点可以成功匹配整个单词，则返回 True。

# DFS 递归逻辑（dfs 方法）：
# 1.边界检查：跳出越界的位置。
# 2.访问检查：当前字符已经访问（标记为 #）则跳过。
# 3.字符不匹配：直接返回 False。
# 4.字符匹配且是最后一个字符：说明单词找到了，返回 True。
# 5.递归搜索四个方向：上、下、左、右。
# 6.回溯：恢复原字符，继续其他路径尝试。
