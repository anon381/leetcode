class Solution:
    def projectionArea(self, grid):
        hor = sum(map(max, grid))
        ver = sum(map(max, zip(*grid)))
        top = sum(v > 0 for row in grid for v in row)
        return ver + hor + top
        
# or in cpp
    # int projectionArea(const vector<vector<int>>& grid) {
    #     int res = 0, n = grid.size(), x, y;
    #     for (int i = 0; i < n; ++i) {
    #         x = 0, y = 0;
    #         for (int j = 0; j < n; ++j) {
    #             x = max(x, grid[i][j]);
    #             y = max(y, grid[j][i]);
    #             if (grid[i][j]) ++res;
    #         }
    #         res += x + y;
    #     }
    #     return res;
    # }
