#  Time Complexity

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):
            
            if word in backward and backward[word] != i:
                res.append([i, backward[word]])
                
            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])
                
            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[j:] == word[:j-1:-1]:
                    res.append([i, backward[word[:j]]])
                    
        return res



#in cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        unordered_map<string, int> backward;
        vector<vector<int>> res;

        // Store reversed words
        for (int i = 0; i < words.size(); i++) {
            string rev = words[i];
            reverse(rev.begin(), rev.end());
            backward[rev] = i;
        }

        for (int i = 0; i < words.size(); i++) {
            string word = words[i];

            // Case 1: Direct reverse match
            if (backward.count(word) && backward[word] != i) {
                res.push_back({i, backward[word]});
            }

            // Case 2: Empty string + palindrome word
            if (!word.empty() && backward.count("") && isPalindrome(word)) {
                res.push_back({i, backward[""]});
                res.push_back({backward[""], i});
            }

            // Case 3: Prefix/suffix palindrome splits
            for (int j = 0; j < word.size(); j++) {
                string suffix = word.substr(j);
                string prefix = word.substr(0, j);

                if (backward.count(suffix) && isPalindrome(prefix)) {
                    res.push_back({backward[suffix], i});
                }
                if (backward.count(prefix) && isPalindrome(suffix)) {
                    res.push_back({i, backward[prefix]});
                }
            }
        }
        return res;
    }

private:
    bool isPalindrome(const string& s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (s[l++] != s[r--]) return false;
        }
        return true;
    }
};






#in java
import java.util.*;

class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        Map<String, Integer> backward = new HashMap<>();
        List<List<Integer>> res = new ArrayList<>();

        // Store reversed words
        for (int i = 0; i < words.length; i++) {
            backward.put(new StringBuilder(words[i]).reverse().toString(), i);
        }

        for (int i = 0; i < words.length; i++) {
            String word = words[i];

            // Case 1: Direct reverse match
            if (backward.containsKey(word) && backward.get(word) != i) {
                res.add(Arrays.asList(i, backward.get(word)));
            }

            // Case 2: Empty string + palindrome word
            if (!word.isEmpty() && backward.containsKey("") && isPalindrome(word)) {
                res.add(Arrays.asList(i, backward.get("")));
                res.add(Arrays.asList(backward.get(""), i));
            }

            // Case 3: Prefix/suffix palindrome splits
            for (int j = 0; j < word.length(); j++) {
                // If suffix is a reversed word and prefix is palindrome
                if (backward.containsKey(word.substring(j)) && isPalindrome(word.substring(0, j))) {
                    res.add(Arrays.asList(backward.get(word.substring(j)), i));
                }
                // If prefix is a reversed word and suffix is palindrome
                if (backward.containsKey(word.substring(0, j)) && isPalindrome(word.substring(j))) {
                    res.add(Arrays.asList(i, backward.get(word.substring(0, j))));
                }
            }
        }
        return res;
    }

    private boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
}

