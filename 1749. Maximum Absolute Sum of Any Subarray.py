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