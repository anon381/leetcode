
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                prev = max(count, prev)
                count = 1
        return max(prev, count)
# in cpp

# class Solution {
# public:
#     int findLengthOfLCIS(vector<int>& nums) {
#         int res = 1, cur = 1;
#         for (int i = 1; i < nums.size(); ++i) {
#             if (nums[i] > nums[i-1]) ++cur;
#             else cur = 1;
#             res = max(res, cur);
#         }
#         return res;
#     }
# };
