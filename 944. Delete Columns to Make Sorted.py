# Time Complexity: O(n * m), where n is the number of strings and m is the length of each string
# Space Complexity: O(1) extra space

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return len([True for col in zip(*A) if sorted(col) != list(col)])

# C++ version of the above Python code:
#
# #include <vector>
# #include <string>
# using namespace std;
# class Solution {
# public:
#     int minDeletionSize(vector<string>& A) {
#         int count = 0;
#         int n = A.size(), m = A[0].size();
#         for (int col = 0; col < m; ++col) {
#             for (int row = 1; row < n; ++row) {
#                 if (A[row][col] < A[row-1][col]) {
#                     count++;
#                     break;
#                 }
#             }
#         }
#         return count;
#     }
# };

# Java version of the above Python code:
#
# import java.util.*;
# class Solution {
#     public int minDeletionSize(String[] A) {
#         int count = 0;
#         int n = A.length, m = A[0].length();
#         for (int col = 0; col < m; ++col) {
#             for (int row = 1; row < n; ++row) {
#                 if (A[row].charAt(col) < A[row-1].charAt(col)) {
#                     count++;
#                     break;
#                 }
#             }
#         }
#         return count;
#     }
# }