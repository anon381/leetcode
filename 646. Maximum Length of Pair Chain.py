
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        prev = pairs[0]
        res = 1

        for cur in pairs[1:]:
            if cur[0] > prev[1]:
                res += 1
                prev = cur

        return res


#in cpp
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        std::sort(pairs.begin(), pairs.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1];
        });
        std::vector<int> prev = pairs[0];
        int res = 1;
        for (int i = 1; i < pairs.size(); i++) {
            const std::vector<int>& cur = pairs[i];
            if (cur[0] > prev[1]) {
                res++;
                prev = cur;
            }
        }

        return res;        
    }
};


#in java
class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, Comparator.comparingInt(a -> a[1]));

        int[] prev = pairs[0];
        int res = 1;

        for (int i = 1; i < pairs.length; i++) {
            int[] cur = pairs[i];
            if (cur[0] > prev[1]) {
                res++;
                prev = cur;
            }
        }

        return res;        
    }
}
