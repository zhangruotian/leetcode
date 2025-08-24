class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path,res = [],[]
        cols,diag1,diag2 = set(),set(),set()
        self.dfs(n,0,path,res,cols,diag1,diag2)
        ans = []
        for r in res:
            matrix = []
            for i,j in r:
                row = ['.']*n
                row[j] = 'Q'
                row_s = ''.join(row)
                matrix.append(row_s)
            ans.append(matrix)
        return ans

    def dfs(self,n,level,path,res,cols,diag1,diag2):
        if len(path)==n:
            res.append(path[:])
            return 
        for j in range(n):
            if not path or self.can_place(level,j,cols,diag1,diag2):
                path.append((level,j))
                cols.add(j)
                diag1.add(j-level)
                diag2.add(j+level)
                self.dfs(n,level+1,path,res,cols,diag1,diag2)
                path.pop()
                cols.remove(j)
                diag1.remove(j-level)
                diag2.remove(j+level)

    def can_place(self,level,j,cols,diag1,diag2):
        if j in cols:
            return False
        if j-level in diag1:
            return False
        if j+level in diag2:
            return False
        return True
# 回溯即可，第一层随便放，后面的层能放就放，不能放return到上一层。判断can_place的时候，用set把时间优化到O(1).
