"""
Time Complexity: O(N * L), where N is the number of words and L is the average length of the words
"""
"""
Space Complexity: O(N * L), for storing all words in the Trie
"""
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


    # Description:
    # This solution uses a Trie data structure to efficiently check if each word can be built one character at a time by other words in the list.
    # It inserts all words into the Trie, then for each word, checks if all prefixes of the word are present as complete words in the Trie.
    # The longest word that meets this condition (or the lexicographically smallest if there are ties) is returned.

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
# import java.util.*;
# class TrieNode {
#     Map<Character, TrieNode> children = new HashMap<>();
#     boolean end = false;
# }
#
# class Solution {
#     public String longestWord(List<String> words) {
#         TrieNode root = new TrieNode();
#         for (String word : words) {
#             TrieNode cur = root;
#             for (char letter : word.toCharArray()) {
#                 cur.children.putIfAbsent(letter, new TrieNode());
#                 cur = cur.children.get(letter);
#             }
#             cur.end = true;
#         }
#
#         String res = "";
#         for (String word : words) {
#             if (word.length() < res.length()) continue;
#             TrieNode cur = root;
#             for (char letter : word.toCharArray()) {
#                 cur = cur.children.get(letter);
#                 if (cur == null) break;
#             }
#             if (cur != null && cur.end && (word.length() > res.length() || (word.length() == res.length() && word.compareTo(res) < 0))) {
#                 res = word;
#             }
#         }
#         return res;
#     }
# };