class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7

        dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                dp[i][j] = dp[i-1][j-1] * (n - j + 1) % mod
            
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j-k)) % mod
        
        return dp[goal][n]




#in cpp
# class Solution {
# public:
#     int numMusicPlaylists(int n, int goal, int k) {
#         const int MOD = 1000000007;

#         vector<vector<long long>> dp(goal + 1, vector<long long>(n + 1, 0));
#         dp[0][0] = 1;

#         for (int i = 1; i <= goal; i++) {
#             for (int j = 1; j <= min(i, n); j++) {
#                 dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % MOD;

#                 if (j > k) {
#                     dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD;
#                 }
#             }
#         }

#         return dp[goal][n];

#     }
# };



# in java
# class Solution {
#     public int numMusicPlaylists(int n, int goal, int k) {
#         int MOD = 1000000007;

#         int[][] dp = new int[goal + 1][n + 1];
#         dp[0][0] = 1;

#         for (int i = 1; i <= goal; i++) {
#             for (int j = 1; j <= Math.min(i, n); j++) {
#                 dp[i][j] = (int)((long)dp[i - 1][j - 1] * (n - j + 1) % MOD);

#                 if (j > k) {
#                     dp[i][j] = (dp[i][j] + (int)((long)dp[i - 1][j] * (j - k) % MOD)) % MOD;
#                 }
#             }
#         }

#         return dp[goal][n];
#     }
# }
