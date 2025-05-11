# Time Complexity: O(m * n), where m is the length of s and n is the length of p
# Space Complexity: O(m * n), for the DP table
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)  # Get lengths of input string and pattern
        dp = [[False] * (n + 1) for _ in range(m + 1)]  # Initialize DP table
        dp[0][0] = True  # Empty string matches empty pattern
        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':  # If current pattern char is '*'
                dp[0][j] = dp[0][j - 2]  # Check if pattern without this char matches empty string
        # Fill DP table for all substrings of s and p
        for i in range(1, m + 1):  # For each character in s
            for j in range(1, n + 1):  # For each character in p
                if p[j - 1] == '*':  # If current pattern char is '*'
                    # '*' can mean zero occurrence (dp[i][j-2]) or one/more (if previous matches)
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    # Direct match or '.' wildcard
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return dp[m][n]  # Final result: does full string match full pattern

# Function Description:
# This function implements regular expression matching with support for '.' and '*'.
# It uses dynamic programming to build a table where dp[i][j] indicates whether the first i characters of string s
# match the first j characters of pattern p. The function handles the '*' character by considering zero or more
# occurrences of the preceding element, and the '.' character as a wildcard that matches any single character.
# The final result is whether the entire string matches the pattern.

# in cpp:
# class Solution {
# public:
#     bool isMatch(string s, string p) {
#         int m = s.size(), n = p.size();
#         vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
#         dp[0][0] = true;
#         for (int j = 2; j <= n; ++j) {
#             if (p[j - 1] == '*')
#                 dp[0][j] = dp[0][j - 2];
#         }
#         for (int i = 1; i <= m; ++i) {
#             for (int j = 1; j <= n; ++j) {
#                 if (p[j - 1] == '*') {
#                     dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'));
#                 } else {
#                     dp[i][j] = dp[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
#                 }
#             }
#         }
#         return dp[m][n];
#     }
# };



#in java
# import java.util.*;
# class Solution {
#     public boolean isMatch(String s, String p) {
#         int m = s.length(), n = p.length();
#         boolean[][] dp = new boolean[m + 1][n + 1];
#         dp[0][0] = true;
#         for (int j = 2; j <= n; ++j) {
#             if (p.charAt(j - 1) == '*')
#                 dp[0][j] = dp[0][j - 2];
#         }
#         for (int i = 1; i <= m; ++i) {
#             for (int j = 1; j <= n; ++j) {
#                 if (p.charAt(j - 1) == '*') {
#                     dp[i][j] = dp[i][j - 2] || (dp
#                         [i - 1][j] && (s.charAt(i - 1) == p.charAt(j - 2) || p.charAt(j - 2) == '.'));
#                 } else {
#                     dp[i][j] = dp[i - 1][j - 1] && (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '.');
#                 }
#             }
#         }
#         return dp[m][n];
#     }
# }