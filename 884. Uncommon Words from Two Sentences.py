"""
Time Complexity: O(N), where N is the total number of words in both sentences
"""
"""
Space Complexity: O(N), for storing all words and their counts
"""
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
# import java.util.*;
# class Solution {
#     public List<String> uncommonFromSentences(String A, String B) {
#         Map<String, Integer> count = new HashMap<>();
#         String[] words = (A + " " + B).split(" ");
#         for (String word : words) {
#             count.put(word, count.getOrDefault(word, 0) + 1);
#         }
#         List<String> result = new ArrayList<>();
#         for (Map.Entry<String, Integer> entry : count.entrySet()) {
#             if (entry.getValue() == 1) {
#                 result.add(entry.getKey());
#             }
#         }
#         return result;
#     }
# };
