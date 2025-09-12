# Complexity
# Time complexity:
# O(n)

# Space complexity:
# O(1)



class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(((0x208222>>(ord(c)&31))&1) for c in s)
        
#in cpp
# class Solution {
# public:
#     static bool doesAliceWin(string& s) {
#         return any_of(s.begin(), s.end(), [](char c) { return ((0x208222>>(c & 31)) & 1); });
#     }
# };
