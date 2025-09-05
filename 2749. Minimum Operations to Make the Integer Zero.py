# Time Complexity: O(60)=O(1)
# Space Complexity: O(1)


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
        return -1

#in cpp
# class Solution {
# public:
#     int makeTheIntegerZero(int num1, int num2) {
#         for (int k = 1; k <= 60; k++) {
#             long long x = num1 - 1LL * num2 * k;
#             if (x < k) {
#                 return -1;
#             }
#             if (k >= __builtin_popcountll(x)) {
#                 return k;
#             }
#         }
#         return -1;
#     }
# };


#in java
# class Solution {
#     public int makeTheIntegerZero(int num1, int num2) {
#         for (int k = 1; k <= 60; k++) {
#             long x = 1L * num1 - 1L * num2 * k;
#             if (x < k) {
#                 return -1;
#             }
#             if (k >= Long.bitCount(x)) {
#                 return k;
#             }
#         }
#         return -1;
#     }
# }
