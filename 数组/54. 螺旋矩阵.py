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
# 旧代码

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bot, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while bot>=top and right>=left:
            top, bot, left, right = self.spiralCircle(matrix, top, bot, left, right,res)
        return res

    def spiralCircle(self, matrix, top, bot, left, right,res):
        if bot>=top+1 and right>=left+1:
            for j in range(left,right+1):
                res.append(matrix[top][j])
            for i in range(top+1, bot):
                res.append(matrix[i][right])
            for p in range(right, left-1,-1):
                res.append(matrix[bot][p])
            for q in range(bot-1, top, -1):
                res.append(matrix[q][left])
        if bot == top and right>=left:
            for i in range(left, right+1):
                res.append(matrix[top][i])
        if bot>=top+1 and right==left:
            for i in range(top, bot+1):
                res.append(matrix[i][left])
        return top+1,bot-1,left+1,right-1
# 新代码
