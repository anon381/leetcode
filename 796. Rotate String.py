class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s


#in cpp
# class Solution {
# public:
#     bool rotateString(string s, string goal) {
#         if (s.length() != goal.length()) {
#             return false;
#         }
#         return (s + s).find(goal) != string::npos;
#     }
# };
