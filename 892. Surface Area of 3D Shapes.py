class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    total_area += 2
                    total_area += 4 * grid[r][c]
                    if r > 0:
                        total_area -= 2 * min(grid[r][c], grid[r - 1][c])
                    if c > 0:
                        total_area -= 2 * min(grid[r][c], grid[r][c - 1])
        return total_area
        
#in cpp
# class Solution {
# public:
#     int surfaceArea(vector<vector<int>>& grid) {
#         int ans = 0;
#         int n = grid.size();
#         for(int i = 0; i < n; i++){
#             for(int j = 0; j < n; j++){
#                 if(grid[i][j]) ans += 4;
#                 ans += i - 1 < 0 ? 2 * grid[i][j] : abs(grid[i][j] - grid[i - 1][j]);
#                 ans += i + 1 == n ? 2 * grid[i][j] : abs(grid[i][j] - grid[i + 1][j]);
#                 ans += j - 1 < 0 ? 2 * grid[i][j] : abs(grid[i][j] - grid[i][j - 1]);
#                 ans += j + 1 == n ? 2 * grid[i][j] : abs(grid[i][j] - grid[i][j + 1]);
#             }
#         }
#         return ans / 2;
#     }
# };
