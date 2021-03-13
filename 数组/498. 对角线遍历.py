class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return []
        n,m=len(matrix),len(matrix[0])
        times=n*m
        i,j=0,0
        res=[]
        for t in range(times):
            if t%2==0:
                while True:
                    if i>=0 and i<n and j>=0 and j<m:
                        res.append(matrix[i][j])
                        i-=1
                        j+=1
                    elif i<0 and j<m:
                        i+=1
                        break
                    elif j>=m:
                        j-=1
                        i+=2
                        break
            else:
                while True:
                    if i>=0 and i<n and j>=0 and j<m:
                        res.append(matrix[i][j])
                        i+=1
                        j-=1
                    elif i>=n:
                        i-=1
                        j+=2
                        break
                    elif i<n and j<0:
                        j+=1
                        break
        return res
# https://leetcode-cn.com/problems/diagonal-traverse/solution/xiao-bai-kan-guo-lai-zui-zhi-bai-yi-li-jie-ban-ben/





