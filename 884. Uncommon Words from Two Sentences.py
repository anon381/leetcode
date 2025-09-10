class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_s1 = s1.split()
        words_s2 = s2.split()        
        all_words = words_s1 + words_s2        
        word_count = Counter(all_words)        
        return [word for word in word_count if word_count[word] == 1]


# C++ version of the above Python code:
# #include <vector>
# #include <string>
# #include <unordered_map>
# #include <unordered_set>
# using namespace std;
#
# class Solution {
# public:
#     vector<string> uncommonFromSentences(string A, string B) {
#         unordered_map<string, int> count;
#         stringstream ss(A + " " + B);
#         string word;
#         while (ss >> word) {
#             count[word]++;
#         }
#         vector<string> result;
#         for (const auto& entry : count) {
#             if (entry.second == 1) {
#                 result.push_back(entry.first);
#             }
#         }
#         return result;
#     }
# };

# Java version of the above Python code: