class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        
        return res



#in cpp
# class Solution {
# public:
#     vector<int> sortedSquares(vector<int>& nums) {
#         vector<int> res(nums.size(), 0);
#         int left = 0;
#         int right = nums.size() - 1;

#         for (int i = nums.size() - 1; i >= 0; i--) {
#             if (abs(nums[left]) > abs(nums[right])) {
#                 res[i] = nums[left] * nums[left];
#                 left++;
#             } else {
#                 res[i] = nums[right] * nums[right];
#                 right--;
#             }
#         }
#         return res;        
#     }
# };
