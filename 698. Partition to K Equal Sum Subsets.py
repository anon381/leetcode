class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(i, used, cursum):
            if used == DONE:
                return True
            
            for j in range(i, N):
                if used & (1 << j) > 0:
                    continue
                if j > 0 and used & (1 << j - 1) == 0 and nums[j] == nums[j - 1]:
                    continue
                
                if nums[j] + cursum < target:
                    if backtrack(j + 1, used | (1 << j), cursum + nums[j]):
                        return True
                elif nums[j] + cursum == target:
                    if backtrack(0, used | (1 << j), 0):
                        return True
                
                if i == 0:
                    break
            return False

        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        nums.sort(reverse=True)
        N = len(nums)
        DONE = (1 << N) - 1
        print(nums)
        return backtrack(0, 0, 0)




#in cpp
class Solution {
public:
    int len;
    vector<int> nums;
    vector<bool> st;

    bool dfs(int start, int cur, int k) {
        if (!k) return true;
        if (cur == len) return dfs(0, 0, k - 1);
        for (int i = start; i < nums.size(); i ++ ) {
            if (st[i]) continue;
            if (cur + nums[i] <= len) {
                st[i] = true;
                if (dfs(i + 1, cur + nums[i], k)) return true;
                st[i] = false;
            }
            while (i + 1 < nums.size() && nums[i + 1] == nums[i]) i ++ ;
            if (!cur || cur + nums[i] == len) return false;
        }
        return false;
    }
    bool canPartitionKSubsets(vector<int>& _nums, int k) {
        nums = _nums;
        st.resize(nums.size());
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k) return false;
        len = sum / k;
        sort(nums.begin(), nums.end(), greater<int>());
        return dfs(0, 0, k);
    }
};
