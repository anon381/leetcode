class Solution:
    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]        
# in cpp
# public solution 
#     string mostCommonWord(string p, vector<string>& banned) {
#         unordered_set<string> ban(banned.begin(), banned.end());
#         unordered_map<string, int> count;
#         for (auto & c: p) c = isalpha(c) ? tolower(c) : ' ';
#         istringstream iss(p);
#         string w;
#         pair<string, int> res ("", 0);
#         while (iss >> w)
#             if (ban.find(w) == ban.end() && ++count[w] > res.second)
#                 res = make_pair(w, count[w]);
#         return res.first;
#     }
