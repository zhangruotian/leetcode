class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m,n = len(mat), len(mat[0])
        for i in range(m):
            res.extend(self.one_diagonal(mat,i,0,m,n))
        for j in range(1,n):
            res.extend(self.one_diagonal(mat,m-1,j,m,n))
        return res

    def one_diagonal(self,mat,i,j,m,n):
        reverse = False if (i+j)%2 == 0 else True
        path = []
        while i>=0 and j<n:
            path.append(mat[i][j])
            i-=1
            j+=1
        if reverse:
            path.reverse()
        return path 
