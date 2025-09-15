class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words
        res = []
        word1 = set(words[0])
        for char in word1:
            frequency = min([word.count(char) for word in words])
            res += [char] * frequency
        return res


#in cpp
# class Solution {
# public:
#     vector<string> commonChars(vector<string>& words) {
#         vector<string> res;
        
#         sort(words.begin(), words.end());
        
#         for (char c : words[0]) {
#             bool common = true;
            
#             for (int i = 1; i < words.size(); i++) {
#                 if (words[i].find(c) == string::npos) {
#                     common = false;
#                     break;
#                 } else {
#                     words[i].erase(words[i].find(c), 1);
#                 }
#             }
#             if (common) {
#                 res.push_back(string(1, c));
#             }
#         }
#         return res;
#     }
# };
