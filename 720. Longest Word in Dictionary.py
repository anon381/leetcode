class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            cur = root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            cur.end = True
            
        res = ''
        for word in words:
            if len(word) < len(res): continue
            cur = root
            for letter in word:
                cur = cur.children[letter]
                if not cur.end: break
            if cur.end and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word        
        return res



# C++ version of the above Python code:
# #include <vector>
# #include <string>
# #include <unordered_map>
# using namespace std;
#
# class TrieNode {
# public:
#     unordered_map<char, TrieNode*> children;
#     bool end = false;
# };
#
# class Solution {
# public:
#     string longestWord(vector<string>& words) {
#         TrieNode* root = new TrieNode();
#         for (const string& word : words) {
#             TrieNode* cur = root;
#             for (char letter : word) {
#                 if (cur->children.find(letter) == cur->children.end()) {
#                     cur->children[letter] = new TrieNode();
#                 }
#                 cur = cur->children[letter];
#             }
#             cur->end = true;
#         }
#
#         string res = "";
#         for (const string& word : words) {
#             if (word.length() < res.length()) continue;
#             TrieNode* cur = root;
#             for (char letter : word) {
#                 cur = cur->children[letter];
#                 if (!cur) break;
#             }
#             if (cur && cur->end && (word.length() > res.length() || (word.length() == res.length() && word < res))) {
#                 res = word;
#             }
#         }
#         return res;
#     }
# };

# Java version of the above Python code: