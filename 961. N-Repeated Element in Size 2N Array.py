class Solution:
    def repeatedNTimes(self, A):
        while 1:
            s = random.sample(A, 2)
            if s[0] == s[1]:
                return s[0]

# C++ version of the above Python code:
#
# #include <vector>
# #include <unordered_set>
# using namespace std;
# class Solution {
# public:
#     int repeatedNTimes(vector<int>& A) {
#         unordered_set<int> seen;
#         for (int num : A) {
#             if (seen.count(num)) return num;
#             seen.insert(num);
#         }
#         return -1; // Should not reach here
#     }
# };
#
# Java version of the above Python code:
#
# import java.util.*;
# class Solution {
#     public int repeatedNTimes(int[] A) {
#         Set<Integer> seen = new HashSet<>();
#         for (int num : A) {
#             if (seen.contains(num)) return num;
#             seen.add(num);
#         }
#         return -1; // Should not reach here
#     }
# }
#