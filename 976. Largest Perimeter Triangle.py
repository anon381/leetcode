class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True) 
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

# in cpp

# #include <bits/stdc++.h>
# using namespace std;

# class Solution {
# public:
#     int largestPerimeter(vector<int>& nums) {
#         sort(nums.rbegin(), nums.rend()); // Sort in descending order
#         for (int i = 0; i < nums.size() - 2; i++) {
#             if (nums[i+1] + nums[i+2] > nums[i]) {
#                 return nums[i] + nums[i+1] + nums[i+2];
#             }
#         }
#         return 0;
#     }
# };


