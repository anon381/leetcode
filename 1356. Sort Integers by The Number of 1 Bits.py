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
# Java version of the above Python code:
#
# import java.util.*;
# class Solution {
#     public int[] sortByBits(int[] arr) {
#         Integer[] boxed = Arrays.stream(arr).boxed().toArray(Integer[]::new);
#         Arrays.sort(boxed, (a, b) -> {
#             int ba = Integer.bitCount(a), bb = Integer.bitCount(b);
#             return ba == bb ? a - b : ba - bb;
#         });
#         for (int i = 0; i < arr.length; i++) {
#             arr[i] = boxed[i];
#         }
#         return arr;
#     }
# }
#