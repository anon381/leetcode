# Time Complexity: O(n log n), where n is the length of arr (due to sorting and mapping)
# Space Complexity: O(n) for the map and sorted array

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        value_to_rank = {}  
        sorted_unique_numbers = sorted(list(set(arr)))  
        
        for index in range(len(sorted_unique_numbers)): 
            value_to_rank[sorted_unique_numbers[index]] = index + 1
          
        for index in range(len(arr)): 
            arr[index] = value_to_rank[arr[index]]

        return arr

# C++ version of the above Python code:
#
# #include <vector>
# #include <algorithm>
# #include <unordered_map>
# using namespace std;
# class Solution {
# public:
#     vector<int> arrayRankTransform(vector<int>& arr) {
#         vector<int> sorted = arr;
#         sort(sorted.begin(), sorted.end());
#         sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
#         unordered_map<int, int> valueToRank;
#         for (int i = 0; i < sorted.size(); ++i) {
#             valueToRank[sorted[i]] = i + 1;
#         }
#         for (int& num : arr) {
#             num = valueToRank[num];
#         }
#         return arr;
#     }
# };

# Java version of the above Python code:
#
# import java.util.*;
# class Solution {
#     public int[] arrayRankTransform(int[] arr) {
#         int[] sorted = arr.clone();
#         Arrays.sort(sorted);
#         Map<Integer, Integer> valueToRank = new HashMap<>();
#         int rank = 1;
#         for (int num : sorted) {
#             if (!valueToRank.containsKey(num)) {
#                 valueToRank.put(num, rank++);
#             }
#         }
#         for (int i = 0; i < arr.length; i++) {
#             arr[i] = valueToRank.get(arr[i]);
#         }
#         return arr;
#     }
# }