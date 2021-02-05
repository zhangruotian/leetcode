class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        left,top=0,0
        bottom=len(matrix)-1
        right=len(matrix[0])-1
        while left<=right and top<=bottom:
            if left<right and top<bottom:
                res+=matrix[top][left:right+1]
                for i in range(top+1,bottom):
                    res.append(matrix[i][right])
                res+=matrix[bottom][left:right+1][::-1]
                for i in range(bottom-1,top,-1):
                    res.append(matrix[i][left])
            if top==bottom and left<=right:
                res+=matrix[top][left:right+1]
            if left==right and top<bottom:
                for i in range(top,bottom+1):
                    res.append(matrix[i][left])
            left+=1
            top+=1
            right-=1
            bottom-=1
        return res
# 定义left right top bottom, 读取最外圈后都--
# 判断条件:left<=right top<=bottom
# 情况:1 left<right and top<bottom: 读一圈
# 1 2 3
# 1 2 3
# 1 2 3
# 情况2: 1 2 3  或者 1  读一行
# 情况3： 读一列
# 1
# 2
# 3 
# 读行的时候由left和right限制长度，读列的时候由top和bottom限制长度

# 时间复杂度O(mn) 空间O(1)