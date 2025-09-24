class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res

#in cpp
class Solution {
public:
    int longestWPI(vector<int>& hours) {
        unordered_map<int, int> seen;
        int score = 0, res = 0;
        for (int i = 0, n = hours.size(); i < n; ++i) {
            if(hours[i] > 8) ++score;
            else --score;
            if (score > 0) res = i + 1;
            else if (seen.count(score - 1)) res = max(res, i - seen[score - 1]);
            if (!seen.count(score)) seen[score] = i;
        }
        return res;
    }
};
