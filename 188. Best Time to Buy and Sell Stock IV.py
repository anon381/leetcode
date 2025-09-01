class Solution:
    def maxProfit(self, k: int, a: List[int]) -> int:
        n=len(a)
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]
        for j in range(1,k+1):
            dp[0][j][1] = -a[0]
        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + a[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - a[i])
        return dp[n-1][k][0]
