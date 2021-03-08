class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0]*n for _ in range(n)]
        top_left=0
        self.num=1
        while top_left<((n+1)//2):
            self.fill(res,top_left,n)
            top_left+=1
        return res
    
    def fill(self,res,top_left,n):
        bot_right=n-top_left
        for i in range(top_left,bot_right):
            res[top_left][i]=self.num
            self.num+=1
        for i in range(top_left+1,bot_right):
            res[i][bot_right-1]=self.num
            self.num+=1
        for i in range(bot_right-2,top_left,-1):
            res[bot_right-1][i]=self.num
            self.num+=1
        for i in range(bot_right-1,top_left,-1):
            res[i][top_left]=self.num
            self.num+=1