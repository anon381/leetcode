class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        if nums[-1] > len(nums):
            return len(nums)
        
        if nums[0] == 0:
            return -1
        
        l = 0
        r = len(nums) - 1
        m = 0
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > m:
                l = m + 1
            elif nums[m] < m:
                r = m - 1
            else:
                return -1
        
        return m + 1 if nums[m] > m else m

#in cpp
class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        int n = nums.size();
        
        if (nums[n - 1] > n) return n;
        if (nums[0] == 0) return -1;

        int l = 0, r = n - 1, m = 0;
        while (l <= r) {
            m = l + (r - l) / 2;
            if (nums[m] > m) {
                l = m + 1;
            } else if (nums[m] < m) {
                r = m - 1;
            } else {
                return -1;
            }
        }
        return nums[m] > m ? m + 1 : m;
    }
};

#in java
class Solution {
    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        
        if (nums[0] >= n) return n;
        
        for (int i = 1; i <= n; i++) {
            if (nums[n - i] >= i && (n - i - 1 < 0 || nums[n - i - 1] < i)) {
                return i;
            }
        }
        
        return -1;
    }
}
