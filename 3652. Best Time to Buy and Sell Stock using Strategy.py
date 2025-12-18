
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k // 2
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + strategy[i] * prices[i]
        
        window_sum = sum(prices[half:k])
        max_profit = max(prefix_sum[n], window_sum + prefix_sum[n] - prefix_sum[k])
        
        for start in range(1, n - k + 1):
            window_sum += prices[start + k - 1] - prices[start + half - 1]
            max_profit = max(max_profit, window_sum + prefix_sum[n] - prefix_sum[start + k] + prefix_sum[start])
        
        return max_profit
