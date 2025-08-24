from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len - 1

# in cpp if needed 
# #include <bits/stdc++.h>
# using namespace std;

# class Solution {
# public:
#     int longestSubarray(vector<int>& nums) {
#         int left = 0, zeros = 0, max_len = 0;
        
#         for (int right = 0; right < nums.size(); right++) {
#             if (nums[right] == 0) zeros++;
            
#             while (zeros > 1) {
#                 if (nums[left] == 0) zeros--;
#                 left++;
#             }
            
#             max_len = max(max_len, right - left + 1);
#         }
        
#         // Subtract 1 because one element must always be deleted
#         return max_len - 1;
#     }
# };
