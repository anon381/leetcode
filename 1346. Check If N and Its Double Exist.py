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