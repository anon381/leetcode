class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n, dirs = len(grid), len(grid[0]), [(0, 1), (1, 1), (-1, 1)]
        @cache
        def dp(i, j):
            ans = 0
            for x, y in dirs:
                ni, nj = i + x, j + y
                if 0 <= ni < m and nj < n and grid[i][j] < grid[ni][nj]:
                    ans = max(ans, 1 + dp(ni, nj))
            return ans
        return max(dp(i, 0) for i in range(m))
# in cpp
# int maxMoves(vector<vector<int>>& grid) {
#     int m = grid.size(), n = grid[0].size();
#     vector<pair<int, int>> dirs = {{0, 1}, {1, 1}, {-1, 1}};
#     vector<vector<int>> cache(m, vector<int>(n, -1));

#     function<int(int, int)> dp = [&](int i, int j) {
#         if (cache[i][j] != -1) return cache[i][j];
#         int ans = 0;
#         for (auto [x, y] : dirs) {
#             int ni = i + x, nj = j + y;
#             if (ni >= 0 && ni < m && nj < n && grid[i][j] < grid[ni][nj])
#                 ans = max(ans, 1 + dp(ni, nj));
#         }
#         return cache[i][j] = ans;
#     };
#     int res = 0;
#     for (int i = 0; i < m; i++)
#         res = max(res, dp(i, 0));
#     return res;
# }


# in java
# class Solution {
#     int dirs[][] = {{0, 1}, {1, 1}, {-1, 1}}, m, n, cache[][];
#     public int maxMoves(int[][] grid) {
#         m = grid.length; n = grid[0].length; cache = new int[m][n];
#         Arrays.stream(cache).forEach(row -> Arrays.fill(row, -1));

#         int res = 0;
#         for (int i = 0; i < m; i++)
#             res = Math.max(res, dp(grid, i, 0));
#         return res;
#     }
    
#     private int dp(int[][] grid, int i, int j) {
#         if (cache[i][j] != -1) return cache[i][j];
#         int ans = 0;
#         for (int[] dir : dirs) {
#             int ni = i + dir[0], nj = j + dir[1];
#             if (ni >= 0 && ni < m && nj < n && grid[i][j] < grid[ni][nj])
#                 ans = Math.max(ans, 1 + dp(grid, ni, nj));
#         }
#         return cache[i][j] = ans;
#     }
# }
