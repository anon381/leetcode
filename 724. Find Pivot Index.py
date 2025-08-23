from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        
        return -1

# or additional cpp code piece 
# #include <vector>
# using namespace std;

# class Solution {
# public:
#     int pivotIndex(vector<int>& nums) {
#         int total = 0;
#         for(int x : nums) total += x;

#         int leftSum = 0;
#         for(int i = 0; i < nums.size(); i++) {
#             int rightSum = total - leftSum - nums[i];
#             if(leftSum == rightSum) return i;
#             leftSum += nums[i];
#         }
#         return -1;
#     }
# };
