# Complexity

# Time complexity = O(n)
# Space complexity = O(1)

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = [0] * 100
        res = 0
        for a, b in dominoes:
            val = a * 10 + b if a < b else b * 10 + a
            res += count[val]
            count[val] += 1
        return res


#in cpp
class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        vector<int> num(100);
        int ret = 0;
        for (auto& it : dominoes) {
            int val = it[0] < it[1] ? it[0] * 10 + it[1] : it[1] * 10 + it[0];
            ret += num[val];
            num[val]++;
        }
        return ret;
    }
};



#in java
