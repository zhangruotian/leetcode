class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        #dp[i][j] 以A[i] B[j]结尾的字串的公共长度
        #if A[i]==B[j]: dp[i][j]=dp[i-1][j-1]+1
        #else:dp[i][j]=0
        n1,n2=len(A),len(B)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        res=0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    if dp[i][j]>res:
                        res=dp[i][j]
        return res

