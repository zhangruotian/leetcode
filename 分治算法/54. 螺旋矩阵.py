class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row=len(matrix)
        if row==0 or len(matrix[0])==0:
            return []
        col=len(matrix[0])
        if row==1:
            return matrix[0]
        if col==1:
            return [matrix[i][0] for i in range(row)]
            
        res=matrix[0]
        for i in range(1,row):
            res.append(matrix[i][col-1])

        for i in range(col-2,-1,-1):
            res.append(matrix[row-1][i])
        
        for i in range(row-2,0,-1):
            res.append(matrix[i][0])

        new_matrix=[]
        for i in range(1,row-1):
            new_matrix.append(matrix[i][1:col-1])
        
        return res + self.spiralOrder(new_matrix)
# 分治