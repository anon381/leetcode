class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [0] * (n + 1)

        for j in range(1, n + 1):
            dp[j] = dp[j - 1] + ord(s2[j - 1])
        
        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] += ord(s1[i - 1])

            for j in range(1, n + 1):
                temp = dp[j]

                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j] + ord(s1[i - 1]), dp[j - 1] + ord(s2[j - 1]))
                
                prev = temp
        
        return dp[n]




#in cpp
class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int m = s1.length();
        int n = s2.length();
        vector<int> dp(n + 1, 0);
        for (int j = 1; j <= n; j++) {
            dp[j] = dp[j - 1] + s2[j - 1];
        }
        for (int i = 1; i <= m; i++) {
            int prev = dp[0];
            dp[0] += s1[i - 1];

            for (int j = 1; j <= n; j++) {
                int temp = dp[j];

                if (s1[i - 1] == s2[j - 1]) {
                    dp[j] = prev;
                } else {
                    dp[j] = min(dp[j] + s1[i - 1], dp[j - 1] + s2[j - 1]);
                }

                prev = temp;
            }
        }
        return dp[n];        
    }
};




#in java
class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        int[] dp = new int[n + 1];

        for (int j = 1; j <= n; j++) {
            dp[j] = dp[j - 1] + s2.charAt(j - 1);
        }
        for (int i = 1; i <= m; i++) {
            int prev = dp[0];
            dp[0] += s1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[j] = prev;
                } else {
                    dp[j] = Math.min(dp[j] + s1.charAt(i - 1), dp[j - 1] + s2.charAt(j - 1));
                }
                prev = temp;
            }
        }
        return dp[n];        
    }
}


#in JavaScript
