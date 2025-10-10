
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        result = float('-inf')
        for i in range(n - 1, -1, -1):
            dp[i] = energy[i] + (dp[i + k] if i + k < n else 0)
            result = max(result, dp[i])
        return result

#in cpp
class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        int n = energy.size();
        vector<int> dp(n);
        int result = INT_MIN;
        for (int i = n - 1; i >= 0; --i) {
            dp[i] = energy[i] + ((i + k < n) ? dp[i + k] : 0);
            result = max(result, dp[i]);
        }
        return result;
    }
};

#in java
class Solution {
    public int maximumEnergy(int[] energy, int k) {
        int l = energy.length;
        int[] dp = new int[l];
        int result = Integer.MIN_VALUE;
        for (int i = l - 1; i >= 0; i--) {
            dp[i] = energy[i] + (i + k < l ? dp[i + k] : 0);
            result = Math.max(result, dp[i]);
        }
        return result;
    }
}
