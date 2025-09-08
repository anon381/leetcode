class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            left = i
            right = n - i
            if '0' not in str(left) and '0' not in str(right):
                return [left, right]
        return []

#in cpp
# class Solution {
# public:
#     vector<int> getNoZeroIntegers(int n) {
#         for (int i = 1; i < n; i++) {
#             int left = i;
#             int right = n - i;
#             if (!containsZero(left) && !containsZero(right)) {
#                 return {left, right};
#             }
#         }
#         return {};
#     }

#     bool containsZero(int n) {
#         string str = to_string(n);
#         return str.find('0') != string::npos;
#     }
# };

#in java
