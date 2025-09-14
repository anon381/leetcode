class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        output = 0
        for i in range(n):
            index = {}
            s = set()
            for j in range(n):
                if i == j:
                    continue
                d = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                if d in s:
                    index[d] += 1
                else:
                    index[d] = 1
                    s.add(d)
            for k in index:
                output += index[k]*(index[k]-1)
        return output 


#in cpp
# class Solution {
# public:
#     int numberOfBoomerangs(vector<vector<int>>& points) {
#         int res = 0, n = points.size();
#         for (int i = 0; i < n; ++i) {
#             unordered_map<int, int> map;
#             for (int j = 0; j < n; ++j) {
#                 if (i == j) continue;
#                 int dx = points[i][0] - points[j][0];
#                 int dy = points[i][1] - points[j][1];
#                 int distSquared = dx * dx + dy * dy;
#                 ++map[distSquared];
#             }
#             for (auto& [dist, count] : map) res += count * (count - 1);
#         }
#         return res;
#     }
# };
