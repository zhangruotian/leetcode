from collections import Counter
class DetectSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        cx,cy = point
        res = 0
        for x,y in self.points.keys():
            diff_x,diff_y = cx-x, cy-y
            if diff_x==diff_y and diff_x>0:
                res+=self.points[(x,cy)]*self.points[(cx,y)]*self.points[(x,y)]
            if diff_x==diff_y and diff_x<0:
                res+=self.points[(cx,y)]*self.points[(x,cy)]*self.points[(x,y)]
            if diff_x==-diff_y and diff_y>0:
                res+=self.points[(cx,y)]*self.points[(x,cy)]*self.points[(x,y)]
            if diff_x==-diff_y and diff_x>0:
                res+=self.points[(x,cy)]*self.points[(cx,y)]*self.points[(x,y)]
        return res

# 先找到对角线上的点，然后可以算出另外两个点，去dict里面查，算结果即可。
