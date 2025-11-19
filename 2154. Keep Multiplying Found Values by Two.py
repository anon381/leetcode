class Solution:
    def findFinalValue(self, nums: list[int], k: int) -> int:
        bits = 0
        for num in nums:
            if num % k != 0:
                continue
            n = num // k
            if n & (n - 1) == 0:
                bits |= n
        d = bits + 1
        return k * (d & -d)

#in cpp
class Solution {
public:
    int findFinalValue(vector<int>& nums, int k) {
        int bits = 0;
        for (auto& n : nums) {
            if (n % k != 0) continue;
            n = n / k;
            if ((n & (n - 1)) == 0)
                bits |= n;
        }
        int d = bits + 1;
        return k * (d & -d);
    }
};
