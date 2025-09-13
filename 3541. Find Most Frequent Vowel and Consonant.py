class Solution:
    def maxFreqSum(self, s: str) -> int:
        con = 0
        vow = 0
        d_set = set(s)
        for i in d_set:
            if i in "aeiou":
                vow = max(vow, s.count(i))
            else:
                con = max(con, s.count(i))
        return con+vow 


#in cpp
# class Solution {
# public:
#     int maxFreqSum(std::string s) {
#         std::unordered_map<char, int> freq;
#         int con = 0, vow = 0;
#         for (char c : s) freq[c]++;
#         for (auto& [ch, count] : freq) {
#             if (std::string("aeiou").find(ch) != std::string::npos)
#                 vow = std::max(vow, count);
#             else
#                 con = std::max(con, count);
#         }
#         return con + vow;
#     }
# };
