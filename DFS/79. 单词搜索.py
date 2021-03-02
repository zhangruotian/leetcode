class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col=len(board),len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    visited=[[0]*col for _ in range(row)]
                    if self.dfs(board,word,0,i,j,visited):
                        return True
        return False
    
    def dfs(self,board,word,index,row,col,visited):
        if row>len(board)-1 or row<0:
            return False
        if col>len(board[0])-1 or col<0:
            return False
        if visited[row][col]:
            return False
        if board[row][col]!=word[index]:
            return False
        if index==len(word)-1:
            return True
        visited[row][col]=1
        up=self.dfs(board,word,index+1,row+1,col,visited)
        if up:return True
        down=self.dfs(board,word,index+1,row-1,col,visited)
        if down:return True
        left=self.dfs(board,word,index+1,row,col-1,visited)
        if left:return True
        right=self.dfs(board,word,index+1,row,col+1,visited)
        if right:return True
        visited[row][col]=0
        return False
# 注意需要用visited记录访问过的，防止往回走
# 记住撤销visited，防止对后面造成影响(与回溯一样，递归后撤销path和visited)
# 记得提前阻断，否则会超时。有一个为true，后面不用看了。