# Time Complexity: O(n), where n is the length of s
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        def ways1(ch):
            if ch == '*': return 9
            if ch == '0': return 0
            return 1

        def ways2(ch1, ch2):
            if ch1 == '*' and ch2 == '*':
                return 15  # 11–19 and 21–26
            if ch1 == '*':
                if '0' <= ch2 <= '6':
                    return 2  # 10–16 or 20–26
                else:
                    return 1  # 17–19
            if ch2 == '*':
                if ch1 == '1':
                    return 9  # 11–19
                if ch1 == '2':
                    return 6  # 21–26
                return 0
            # both digits
            num = int(ch1 + ch2)
            return 1 if 10 <= num <= 26 else 0

        n = len(s)
        if n == 0:
            return 0

        dp0, dp1 = 1, ways1(s[0])  # dp[0], dp[1]

        for i in range(1, n):
            single = ways1(s[i]) * dp1
            double = ways2(s[i-1], s[i]) * dp0
            dp0, dp1 = dp1, (single + double) % MOD

        return dp1

# C++ version 
# #include <string>
# #include <vector>
# using namespace std;
# class Solution {
# public:
#     int numDecodings(string s) {
#         const int MOD = 1e9 + 7;
#         int n = s.size();
#         if (n == 0) return 0;
#         long dp0 = 1, dp1 = ways1(s[0]);
#         for (int i = 1; i < n; ++i) {
#             long single = ways1(s[i]) * dp1;
#             long double = ways2(s[i-1], s[i]) * dp0;
#             dp0 = dp1;
#             dp1 = (single + double) % MOD;
#         }
#         return dp1;
#     }
# };

#java version
# import java.util.*;
# class Solution {
#     public int numDecodings(String s) {
#         final int MOD = 1_000_000_007;
#         int n = s.length();
#         if (n == 0) return 0;
#         long dp0 = 1, dp1 = ways1(s.charAt(0));
#         for (int i = 1; i < n; ++i) {
#             long single = ways1(s.charAt(i)) * dp1;
#             long double = ways2(s.charAt(i-1), s.charAt(i)) * dp0;
#             dp0 = dp1;
#             dp1 = (single + double) % MOD;
#         }
#         return (int) dp1;
#     }
# };
