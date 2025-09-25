
class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        for i in range(len(tri) - 2, -1, -1):
            for j in range(len(tri[i])):
                tri[i][j] += min(tri[i + 1][j], tri[i + 1][j + 1])
        return tri[0][0]

# in cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        for (int i = triangle.size() - 2; i >= 0; i--)
            for (int j = 0; j < triangle[i].size(); j++)
                triangle[i][j] +=
                    min(triangle[i + 1][j], triangle[i + 1][j + 1]);

        return triangle[0][0];
    }
};


#in java
class Solution {
    public int minimumTotal(List<List<Integer>> tri) {
        for (int i = tri.size() - 2; i >= 0; i--)
            for (int j = 0; j < tri.get(i).size(); j++)
                tri.get(i).set(j, tri.get(i).get(j) + Math.min(
                    tri.get(i + 1).get(j),
                    tri.get(i + 1).get(j + 1)
                ));
        return tri.get(0).get(0);
    }
}
