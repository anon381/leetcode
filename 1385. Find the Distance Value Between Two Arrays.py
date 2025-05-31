# Time Complexity: O(n log m), where n is len(arr1) and m is len(arr2) (due to binary search for each element)
# Space Complexity: O(1) extra space (in-place sort)

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0

        for num in arr1:
            left_index = bisect.bisect_left(arr2, num - d)
            right_index = bisect.bisect_right(arr2, num + d)

            if left_index == right_index:
                count += 1
        
        return count

# C++ version of the above Python code:
#
# #include <vector>
# #include <algorithm>
# #include <cmath>
# using namespace std;
#
# class Solution {
# public:
#     int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
#         sort(arr2.begin(), arr2.end());
#         int count = 0;
#         for (int num : arr1) {
#             auto left = lower_bound(arr2.begin(), arr2.end(), num - d);
#             auto right = upper_bound(arr2.begin(), arr2.end(), num + d);
#             if (left == right) {
#                 count++;
#             }
#         }
#         return count;
#     }
# };

# Java version of the above Python code:
#
# import java.util.*;
# class Solution {
#     public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
#         Arrays.sort(arr2);
#         int count = 0;
#         for (int num : arr1) {
#             int left = Arrays.binarySearch(arr2, num - d);
#             int right = Arrays.binarySearch(arr2, num + d);
#             left = left < 0 ? -(left + 1) : left;
#             right = right < 0 ? -(right + 1) : right + 1;
#             if (left == right) {
#                 count++;
#             }
#         }
#         return count;
#     }
# }


