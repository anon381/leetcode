class Solution:
    def shortestSuperstring(self, words):
        n = len(words)
        
        # Compute overlap[i][j] = maximum suffix of i that is prefix of j


        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    m = min(len(words[i]), len(words[j]))
                    for k in range(m, 0, -1):
                        if words[i].endswith(words[j][:k]):
                            overlap[i][j] = k
                            break
                      # DP[mask][i] = shortest superstring ending with words[i], using mask set
        dp = [[""]*n for _ in range(1<<n)]
        for i in range(n):
            dp[1<<i][i] = words[i]
        for mask in range(1<<n):
            for j in range(n):
                if not (mask & (1<<j)):
                    continue
                prev_mask = mask ^ (1<<j)
                if prev_mask == 0:
                    continue
                for i in range(n):
                    if not (prev_mask & (1<<i)):
                        continue
                    candidate = dp[prev_mask][i] + words[j][overlap[i][j]:]
                    if dp[mask][j] == "" or len(candidate) < len(dp[mask][j]):
                        dp[mask][j] = candidate
                # Pick the shortest among all full-mask superstrings

        full_mask = (1<<n) - 1
        ans = None
        for i in range(n):
            if ans is None or len(dp[full_mask][i]) < len(ans):
                ans = dp[full_mask][i]
        return ans



#in cpp
# #include <bits/stdc++.h>
# using namespace std;

# class Solution {
# public:
#     string shortestSuperstring(vector<string>& words) {
#         int n = words.size();
#         vector<vector<int>> overlap(n, vector<int>(n, 0));

#         // Compute overlaps
#         for (int i = 0; i < n; i++) {
#             for (int j = 0; j < n; j++) {
#                 if (i == j) continue;
#                 int m = min(words[i].size(), words[j].size());
#                 for (int k = m; k > 0; k--) {
#                     if (words[i].substr(words[i].size() - k) == words[j].substr(0, k)) {
#                         overlap[i][j] = k;
#                         break;
#                     }
#                 }
#             }
#         }

#         // DP[mask][i] = shortest superstring ending with words[i]
#         vector<vector<string>> dp(1 << n, vector<string>(n, ""));
#         for (int i = 0; i < n; i++) dp[1 << i][i] = words[i];

#         for (int mask = 1; mask < (1 << n); mask++) {
#             for (int j = 0; j < n; j++) {
#                 if (!(mask & (1 << j))) continue;
#                 int prevMask = mask ^ (1 << j);
#                 if (prevMask == 0) continue;
#                 for (int i = 0; i < n; i++) {
#                     if (!(prevMask & (1 << i))) continue;
#                     string candidate = dp[prevMask][i] + words[j].substr(overlap[i][j]);
#                     if (dp[mask][j].empty() || candidate.size() < dp[mask][j].size()) {
#                         dp[mask][j] = candidate;
#                     }
#                 }
#             }
#         }

#         // Find answer among all full-mask endings
#         int fullMask = (1 << n) - 1;
#         string ans;
#         for (int i = 0; i < n; i++) {
#             if (ans.empty() || dp[fullMask][i].size() < ans.size())
#                 ans = dp[fullMask][i];
#         }
#         return ans;
#     }
# };




#in java
# import java.util.*;

# class Solution {
#     public String shortestSuperstring(String[] words) {
#         int n = words.length;
#         int[][] overlap = new int[n][n];

#         // Compute overlaps
#         for (int i = 0; i < n; i++) {
#             for (int j = 0; j < n; j++) {
#                 if (i == j) continue;
#                 int m = Math.min(words[i].length(), words[j].length());
#                 for (int k = m; k > 0; k--) {
#                     if (words[i].endsWith(words[j].substring(0, k))) {
#                         overlap[i][j] = k;
#                         break;
#                     }
#                 }
#             }
#         }

#         // DP[mask][i] = shortest superstring ending with words[i]
#         String[][] dp = new String[1 << n][n];
#         for (int i = 0; i < n; i++) dp[1 << i][i] = words[i];

#         for (int mask = 1; mask < (1 << n); mask++) {
#             for (int j = 0; j < n; j++) {
#                 if ((mask & (1 << j)) == 0) continue;
#                 int prevMask = mask ^ (1 << j);
#                 if (prevMask == 0) continue;
#                 for (int i = 0; i < n; i++) {
#                     if ((prevMask & (1 << i)) == 0) continue;
#                     String candidate = dp[prevMask][i] + words[j].substring(overlap[i][j]);
#                     if (dp[mask][j] == null || candidate.length() < dp[mask][j].length()) {
#                         dp[mask][j] = candidate;
#                     }
#                 }
#             }
#         }

#         // Find answer among all full-mask endings
#         int fullMask = (1 << n) - 1;
#         String ans = null;
#         for (int i = 0; i < n; i++) {
#             if (ans == null || dp[fullMask][i].length() < ans.length())
#                 ans = dp[fullMask][i];
#         }
#         return ans;
#     }
# }
