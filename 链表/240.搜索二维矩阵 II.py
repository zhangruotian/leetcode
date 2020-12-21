class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        i=0
        j=n-1
        while i<m and j>-1:
            comp=matrix[i][j]
            if target==comp:
                return True
            if target>comp:
                i+=1
            else:
                j-=1
        return False
# 从右上角(或者左下角)开始搜索，target大于当前值则往下走，小于则往左走
# T:O(m+n) S:O(1)