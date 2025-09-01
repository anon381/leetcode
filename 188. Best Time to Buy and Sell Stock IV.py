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

        

#in cpp
# class Solution {
# public:
#     int maxProfit(int k, vector<int>& prices) {
#         int n = prices.size();
#         if (n == 0) return 0;
#         if (k >= n / 2) {
#             int profit = 0;
#             for (int i = 1; i < n; i++) {
#                 if (prices[i] > prices[i - 1]) 
#                     profit += prices[i] - prices[i - 1];
#             }
#             return profit;
#         }

#         vector<int> buy(k + 1, INT_MIN), sell(k + 1, 0);
#         for (int price : prices) {
#             for (int t = 1; t <= k; t++) {
#                 buy[t] = max(buy[t], sell[t - 1] - price);
#                 sell[t] = max(sell[t], buy[t] + price); 
#             }
#         }
#         return sell[k];
#     }
# };
