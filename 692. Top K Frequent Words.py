class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter

        # Step 1: Count word frequencies
        freq = Counter(words)

        # Step 2: Sort by frequency desc, then lex asc
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        # Step 3: Return top k
        return [word for word, count in sorted_words[:k]]



#in cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> mp;
        for (string& word : words) {
            mp[word]++;
        }

        vector<pair<string, int>> vec;
        for (auto& p : mp) {
            vec.push_back({p.first, p.second});
        }

        // Sort by frequency descending, then lexicographically ascending
        sort(vec.begin(), vec.end(), [](auto& a, auto& b) {
            if (a.second == b.second)
                return a.first < b.first;  // lex smaller comes first
            return a.second > b.second;   // higher freq first
        });

        vector<string> res;
        for (int i = 0; i < k; i++) {
            res.push_back(vec[i].first);
        }
        return res;
    }
};





#in java
