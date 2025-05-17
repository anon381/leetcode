class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def custom_sort_key(num):
            bit_count = bin(num).count('1')
            return (bit_count, num)

        arr.sort(key=custom_sort_key)

        return arr

# C++ version of the above Python code:
#
# #include <vector>
# #include <algorithm>
# using namespace std;
# class Solution {
# public:
#     vector<int> sortByBits(vector<int>& arr) {
#         auto bitCount = [](int num) {
#             int count = 0;
#             while (num) {
#                 count += num & 1;
#                 num >>= 1;
#             }
#             return count;
#         };
#         sort(arr.begin(), arr.end(), [&](int a, int b) {
#             int ba = bitCount(a), bb = bitCount(b);
#             return ba == bb ? a < b : ba < bb;
#         });
#         return arr;
#     }
# };
#