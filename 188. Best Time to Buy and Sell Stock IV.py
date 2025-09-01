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

        # or 

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k==0: return 0
        dp = [[1000,0] for _ in range(k+1)]
        for price in prices:
            for i in range(1,k+1):
                dp[i][0] = min(dp[i][0], price - dp[i-1][1])
                dp[i][1] = max(dp[i][1] , price - dp[i][0])
        return dp[k][1]

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




# in java

# in java 
# class Solution {
#     public int maxProfit(int k, int[] prices) {
#         int[] buy = new int[k + 1];
#         int[] sell = new int[k + 1];

#         for (int i = 1; i <= k; i++) {
#             buy[i] = Integer.MIN_VALUE;
#         }

#         for (int price : prices) {
#             for (int i = 1; i <= k; i++) {
#                 buy[i] = Math.max(buy[i], sell[i - 1] - price);
#                 sell[i] = Math.max(sell[i], buy[i] + price);
#             }
#         }
        
#         return sell[k];
#     }
# }
