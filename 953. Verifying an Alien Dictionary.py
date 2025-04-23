class Solution:
    def isAlienSorted(self, words, order):
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

# C++ version of the above Python code:
#
# #include <vector>
# #include <string>
# #include <unordered_map>
# using namespace std;
# class Solution {
# public:
#     bool isAlienSorted(vector<string>& words, string order) {
#         unordered_map<char, int> m;
#         for (int i = 0; i < order.size(); ++i) m[order[i]] = i;
#         for (int i = 1; i < words.size(); ++i) {
#             string& w1 = words[i-1], &w2 = words[i];
#             int j = 0;
#             while (j < w1.size() && j < w2.size() && w1[j] == w2[j]) ++j;
#             if (j < w1.size() && j < w2.size()) {
#                 if (m[w1[j]] > m[w2[j]]) return false;
#             } else if (w1.size() > w2.size()) return false;
#         }
#         return true;
#     }
# };