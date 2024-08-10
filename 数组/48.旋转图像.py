class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            self.swap_row_col(matrix,i,n)
        self.swap_row(matrix,n)
        return matrix
    
    def swap_row_col(self, matrix, start,n):
        for i in range(start,n):
            matrix[start][i], matrix[i][start] = matrix[i][start], matrix[start][i]
    
    def swap_row(self,matrix,n):
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-1-j] =matrix[i][n-1-j] ,matrix[i][j]



# 先交换行和列（第一行第一列，以此类推），再反转每行。
