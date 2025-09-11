# Time complexity:
# O(n), 
# Space complexity:
# O(1), 


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

#in cpp
# class Solution {
# public:
#     bool checkValidString(string s) {
#         int leftMin = 0, leftMax = 0;

#         for (char c : s) {
#             if (c == '(') {
#                 leftMin++;
#                 leftMax++;
#             } else if (c == ')') {
#                 leftMin--;
#                 leftMax--;
#             } else {
#                 leftMin--;
#                 leftMax++;
#             }
#             if (leftMax < 0) return false;
#             if (leftMin < 0) leftMin = 0;
#         }
        
#         return leftMin == 0;
#     }
# };


#in java
# public class Solution {
#     public boolean checkValidString(String s) {
#         int leftMin = 0, leftMax = 0;

#         for (char c : s.toCharArray()) {
#             if (c == '(') {
#                 leftMin++;
#                 leftMax++;
#             } else if (c == ')') {
#                 leftMin--;
#                 leftMax--;
#             } else {
#                 leftMin--;
#                 leftMax++;
#             }
#             if (leftMax < 0) return false;
#             if (leftMin < 0) leftMin = 0;
#         }
        
#         return leftMin == 0;
#     }
# }
