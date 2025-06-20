class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_has_0 = False
        first_col_has_0 = False
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            if matrix[i][0]==0:
                first_col_has_0=True
        for j in range(n):
            if matrix[0][j]==0:
                first_row_has_0=True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if first_row_has_0:
            for j in range(n):
                matrix[0][j]=0
        if first_col_has_0:
            for i in range(m):
                matrix[i][0]=0
# 1.先检查第一行和第一列有没有 0，用两个标志变量记录下来。
# 2.用第一行和第一列当作“标记位”，标记其他行列是否需要置 0。
# 3.根据标记，把非第一行和第一列里需要变 0 的位置改成 0。
# 4.最后根据最开始的两个标志，决定是否要把第一行和第一列也置 0。
# O(mn) O(1)
