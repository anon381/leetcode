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

#in java
# class Solution {
#     public int surfaceArea(int[][] grid) {
#         int result = 0;
#         for (int i = 0; i < grid.length; i++)    for (int j = 0; j < grid[0].length; j++)    result += getArea(grid, i, j);
#         return result;
#     }
#     private int getArea(int[][] grid, int i, int j) {
#         int towerHeight = grid[i][j];
#         if (towerHeight == 0)    return 0;
#         int area = 2 + (towerHeight * 4);
#         if (i > 0)    area -= Math.min(towerHeight, grid[i - 1][j]);
#         if (i < grid.length - 1)    area -= Math.min(towerHeight, grid[i + 1][j]);
#         if (j > 0)    area -= Math.min(towerHeight, grid[i][j - 1]);
#         if (j < grid[0].length - 1)    area -= Math.min(towerHeight, grid[i][j + 1]);
#         return area;
#     }
# }
