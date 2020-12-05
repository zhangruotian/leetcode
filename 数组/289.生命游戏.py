class Solution:
    def gameOfLife(self, board) :
        """
        Do not return anything, modify board in-place instead.
        """
        # mark live-->dead (-1)
        # mark live-->live  (1)
        # mark dead-->live (2)
        # mark dead-->dead (0)

        h = len(board)
        w = len(board[0])

        def counter(i,j):
            c=0
            for m in range(-1,2):
                for n in range(-1,2):
                    if i+m<0 or j+n <0 :
                        continue
                    if i+m>h-1 or j+n>w-1:
                        continue
                    else:
                        if board[i+m][j+n]==1 or board[i+m][j+n]==-1:
                            c+=1
            return c

        for i in range(h):
            for j in range(w):
                live=counter(i,j)
                if board[i][j] ==1:
                    live=live-1
                    if live<2 or live>3:
                        board[i][j]=-1
                else:
                    if live==3:
                        board[i][j]=2
        for i in range(h):
            for j in range(w):
                if board[i][j]==2:
                    board[i][j]=1
                if board[i][j]==-1:
                    board[i][j]=0
# in-place操作，直接在传入的二维array上操作，不create新的object
# 用其他数字记录前后的状态。根据以前的状态判断新状态，然后更新。最后把marks变为0和1。