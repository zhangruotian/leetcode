class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        res_X = []
        res_O = []
        for i in range(m):
            for j in range(n):
                if board[i][j]!='O':
                    continue
                path = []
                is_surrounded = self.dfs(board,i,j,m,n,path)
                if is_surrounded:
                    res_X.extend(path)
                else:
                    res_O.extend(path)
        for i,j in res_X:
            board[i][j]='X'
        for i,j in res_O:
            board[i][j]='O'
    
    def dfs(self,board,i,j,m,n,path):
        if i<0 or i>=m or j<0 or j>=n:
            return False
        if board[i][j]=='X' or board[i][j]=='V':
            return True
        board[i][j] = 'V'
        path.append((i,j))
        b = self.dfs(board,i+1,j,m,n,path)
        t = self.dfs(board,i-1,j,m,n,path)
        l = self.dfs(board,i,j-1,m,n,path)
        r = self.dfs(board,i,j+1,m,n,path)
        if b and t and l and r:
            return True
        return False
# 遇到O开始搜索，搜索完所有的方向才能知道，这个岛屿应该mark成'X'还是'O'
# 在搜索的途中记录下path，如果是个被围绕的岛屿，最后改为'X'
# 走过的位置改为'V'，后面遇到同一个岛屿的不同位置，不进入dfs。
