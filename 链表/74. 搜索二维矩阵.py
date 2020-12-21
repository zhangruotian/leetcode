class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix==[]:
            return False
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m*n
        while l<r:
            mid=(l+r-1)//2
            index_m=mid//n
            index_n=mid%n
            if matrix[index_m][index_n]==target:
                return True
            if matrix[index_m][index_n]<target:
                l=mid+1
            else:
                r=mid
        return False