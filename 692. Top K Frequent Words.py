
Complexity
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

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
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();

        // Step 1: Count frequencies
        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }

        // Step 2: Transfer to list and sort
        List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());

        list.sort((a, b) -> {
            if (!a.getValue().equals(b.getValue())) {
                return b.getValue() - a.getValue(); // frequency descending
            }
            return a.getKey().compareTo(b.getKey()); // lexicographically ascending
        });

        // Step 3: Collect top k
        List<String> res = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            res.add(list.get(i).getKey());
        }

        return res;
    }
}
