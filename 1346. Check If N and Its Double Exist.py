# Time Complexity: O(n), where n is the length of arr
# Space Complexity: O(n) for the set

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}  

        for num in arr:  
            if (2 * num in seen) or (num % 2 == 0 and num // 2 in seen):
                return True  
            seen[num] = seen.get(num, 0) + 1

        return False

# C++ version of the above Python code:
#
# #include <vector>
# #include <unordered_set>
# using namespace std;
# class Solution {
# public:
#     bool checkIfExist(vector<int>& arr) {
#         unordered_set<int> seen;
#         for (int num : arr) {
#             if (seen.count(2 * num) || (num % 2 == 0 && seen.count(num / 2))) {
#                 return true;
#             }
#             seen.insert(num);
#         }
#         return false;
#     }
# };
#
# Java version of the above Python code:
#
# import java.util.*;
# class Solution {
#     public boolean checkIfExist(int[] arr) {
#         Set<Integer> seen = new HashSet<>();
#         for (int num : arr) {
#             if (seen.contains(2 * num) || (num % 2 == 0 && seen.contains(num / 2))) {
#                 return true;
#             }
#             seen.add(num);
#         }
#         return false;
#     }
# }
#