class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        prev = None
        for i, num in enumerate(nums):
            if num == 1:
                if prev is not None and i - prev <= k:
                    return False
                prev = i
        return True

#kin cpp
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {

        int n = nums.size();
        int pre_index;
        bool f = true;

        for (int i = 0; i < n; i++) {
            if (f && nums[i] == 1) {
                f = false;
                pre_index = i;
                continue;
            }
            if (nums[i] == 1) {
                if (i - pre_index - 1 >= k)
                    pre_index = i;
                else
                    return false;
            }
        }

        return true;
    }
};
