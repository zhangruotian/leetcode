class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m,n = len(matrix),len(matrix[0])
        for i in range(min(m+1,n+1)//2):
            self.spiralone(i,i,matrix,res,m,n)
        return res
    
    def spiralone(self,start_i,start_j,matrix,res,m,n):
        end_i,end_j = m-start_i-1,n-start_j-1
        for j in range(start_j,end_j+1):
            res.append(matrix[start_i][j])
        for i in range(start_i+1,end_i+1):
            res.append(matrix[i][end_j])
        for j in range(end_j-1,start_j-1,-1):
            if start_i!=end_i:
                res.append(matrix[end_i][j])
        for i in range(end_i-1,start_i,-1):
            if start_j!=end_j:
                res.append(matrix[i][start_j])

# 提前算好初始点的位置
# 注意处理剩一行或者一列的情况。
