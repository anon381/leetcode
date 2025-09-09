"""
Time Complexity: O(n), where n is the length of the input array

Space Complexity: O(1), only constant extra space is used
"""
class Solution:
    def maxAbsoluteSum(self, A):
        return max(accumulate(A, initial=0)) - min(accumulate(A, initial=0))        

# C++ version
# class Solution {
# public:
#     int maxAbsoluteSum(vector<int>& A) {
#         int max_sum = 0, min_sum = 0, curr_sum = 0;
#         for (int x : A) {
#             curr_sum += x;
#             max_sum = max(max_sum, curr_sum);
#             min_sum = min(min_sum, curr_sum);
#         }
#         return max_sum - min_sum;
#     }
# };


# Java version
# import java.util.*;
# class Solution {
#     public int maxAbsoluteSum(int[] A) {
#         int max_sum = 0, min_sum = 0, curr_sum = 0;
#         for (int x : A) {
#             curr_sum += x;
#             max_sum = Math.max(max_sum, curr_sum);
#             min_sum = Math.min(min_sum, curr_sum);
#         }
#         return max_sum - min_sum;
#     }
# }
