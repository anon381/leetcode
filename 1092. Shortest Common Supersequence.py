class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        i, j = m, n
        result = []
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                result.append(str1[i-1])
                i -= 1
            else:
                result.append(str2[j-1])
                j -= 1        
        while i > 0:
            result.append(str1[i-1])
            i -= 1        
        while j > 0:
            result.append(str2[j-1])
            j -= 1        
        return ''.join(result[::-1])


#in cpp
# class Solution {
# public:
#     string shortestCommonSupersequence(string str1, string str2) {
#         int m = str1.length();
#         int n = str2.length();
#         vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
#         for (int i = 1; i <= m; i++) {
#             for (int j = 1; j <= n; j++) {
#                 if (str1[i - 1] == str2[j - 1]) {
#                     dp[i][j] = 1 + dp[i - 1][j - 1];
#                 } else {
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
#                 }
#             }
#         }
        
#         int i = m, j = n;
#         string result = "";
        
#         while (i > 0 && j > 0) {
#             if (str1[i - 1] == str2[j - 1]) {
#                 result.push_back(str1[i - 1]);
#                 i--;
#                 j--;
#             } else if (dp[i - 1][j] > dp[i][j - 1]) {
#                 result.push_back(str1[i - 1]);
#                 i--;
#             } else {
#                 result.push_back(str2[j - 1]);
#                 j--;
#             }
#         }
        
#         while (i > 0) {
#             result.push_back(str1[i - 1]);
#             i--;
#         }
        
#         while (j > 0) {
#             result.push_back(str2[j - 1]);
#             j--;
#         }
        
#         reverse(result.begin(), result.end());
        
#         return result;
#     }
# };

#in java
