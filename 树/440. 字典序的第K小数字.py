class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur=1
        while k>1:
            sub_count=self.subtreeCount(cur,n)
            if sub_count+1<=k:
                cur+=1
                k-=sub_count
            else:
                cur*=10
                k-=1
        return cur
    
    def subtreeCount(self,i,n):
        count=0
        level_num=1
        while i<=n:
            count+=min(level_num,n-i+1)
            i*=10
            level_num*=10
        return count
#笔记
#https://www.youtube.com/watch?v=yMnR63e3KLo