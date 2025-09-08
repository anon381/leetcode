# Time Complexity: O(log n), where n is the input number
# Space Complexity: O(1)

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + self.numberOfSteps(num - 1 if num & 1 else num >> 1)

# C++ version of the above Python code:
#
# class Solution {
# public:
#     int numberOfSteps(int num) {
#         int steps = 0;
#         while (num) {
#             if (num % 2 == 0) num /= 2;
#             else num -= 1;
#             steps++;
#         }
#         return steps;
#     }
# };
#
# Java version of the above Python code:
#
# class Solution {
#     public int numberOfSteps(int num) {
#         int steps = 0;
#         while (num != 0) {
#             if (num % 2 == 0) num /= 2;
#             else num -= 1;
#             steps++;
#         }
#         return steps;
#     }
# }
#