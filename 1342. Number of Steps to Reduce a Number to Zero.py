
# Function Description:
# This function calculates the number of steps required to reduce a given number to zero.
# At each step, if the number is even, it is divided by two; if odd, it is decremented by one.
# The process continues recursively until the number reaches zero, counting the steps taken.
#
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