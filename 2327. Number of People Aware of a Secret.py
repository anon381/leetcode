# Time Complexity: O(n), where n is the number of days
# Space Complexity: O(n), for the dp array
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        window = 0
        for i in range(2, n + 1):
            enter = i - delay
            exit_ = i - forget
            if enter >= 1:
                window = (window + dp[enter]) % MOD
            if exit_ >= 1:
                window = (window - dp[exit_] + MOD) % MOD
            dp[i] = window
        start = max(1, n - forget + 1)
        ans = sum(dp[start: n+1]) % MOD
        return ans

# C++ version 
# #include <vector>
# using namespace std;
# class Solution {
# public:
#     int peopleAwareOfSecret(int n, int delay, int forget) {
#         const int MOD = 1e9 + 7;
#         if (n == 1) return 1;
#         vector<int> dp(n + 1, 0);
#         dp[1] = 1;
#         int window = 0;
#         for (int i = 2; i <= n; ++i) {
#             int enter = i - delay;
#             int exit_ = i - forget;
#             if (enter >= 1) {
#                 window = (window + dp[enter]) % MOD;
#             }
#             if (exit_ >= 1) {
#                 window = (window - dp[exit_] + MOD) % MOD;
#             }
#             dp[i] = window;
#         }
#         int start = max(1, n - forget + 1);
#         long long ans = 0;
#         for (int i = start; i <= n; ++i) {
#             ans = (ans + dp[i]) % MOD;
#         }
#         return ans;
#     }
# };


# Java version
# import java.util.*;
# class Solution {
#     public int peopleAwareOfSecret(int n, int delay, int forget) {
#         final int MOD = 1_000_000_007;
#         if (n == 1) return 1;
#         long[] dp = new long[n + 1];
#         dp[1] = 1;
#         long window = 0;
#         for (int i = 2; i <= n; ++i) {
#             int enter = i - delay;
#             int exit_ = i - forget;
#             if (enter >= 1) {
#                 window = (window + dp[enter]) % MOD;
#             }
#             if (exit_ >= 1) {
#                 window = (window - dp[exit_] + MOD) % MOD;
#             }
#             dp[i] = window;
#         }
#         int start = Math.max(1, n - forget + 1);
#         long ans = 0;
#         for (int i = start; i <= n; ++i) {
#             ans = (ans + dp[i]) % MOD;
#         }
#         return (int) ans;
#     }
# };
