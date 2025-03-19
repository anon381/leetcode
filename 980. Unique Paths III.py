# Time Complexity: O(4^k), where k is the number of empty squares
# Space Complexity: O(k), for recursion stack and grid modifications
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = None  
        count = 0  
        for i in range(m):
            for j in range(n):
                count += grid[i][j] == 0
                if not start and grid[i][j] == 1:
                    start = (i, j)
        
        def backtrack(i: int, j: int) -> int:
            nonlocal count
            result = 0
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 0:
                        grid[x][y] = -1
                        count -= 1
                        result += backtrack(x, y)
                        grid[x][y] = 0
                        count += 1
                    elif grid[x][y] == 2:
                        result += count == 0
            return result
        return backtrack(start[0], start[1])




# Description:
# This solution finds all unique paths from the starting square to the ending square in a grid, visiting every empty square exactly once.
# It uses backtracking to explore all possible paths, marking squares as visited and unvisited as it recurses.
# The function counts the number of valid paths that cover all empty squares before reaching the ending square.
# Obstacles are skipped, and the recursion only proceeds to valid, unvisited squares.
# The approach is efficient for small grids due to exponential time complexity, but demonstrates clear recursive logic for pathfinding.


# C++ version:

# class Solution {
# public:
#     int uniquePathsIII(vector<vector<int>>& grid) {
#         int m = grid.size(), n = grid[0].size();
#         int start_i = -1, start_j = -1, empty = 0;
#         for (int i = 0; i < m; ++i) {
#             for (int j = 0; j < n; ++j) {
#                 if (grid[i][j] == 1) {
#                     start_i = i; start_j = j;
#                 }
#                 if (grid[i][j] == 0) ++empty;
#             }
#         }
#         return backtrack(grid, start_i, start_j, empty);
#     }
# private:
#     int backtrack(vector<vector<int>>& grid, int i, int j, int empty) {
#         int m = grid.size(), n = grid[0].size(), res = 0;
#         vector<pair<int, int>> dirs = {{-1,0},{1,0},{0,-1},{0,1}};
#         for (auto& d : dirs) {
#             int x = i + d.first, y = j + d.second;
#             if (x >= 0 && x < m && y >= 0 && y < n) {
#                 if (grid[x][y] == 0) {
#                     grid[x][y] = -1;
#                     --empty;
#                     res += backtrack(grid, x, y, empty);
#                     grid[x][y] = 0;
#                     ++empty;
#                 } else if (grid[x][y] == 2) {
#                     res += empty == 0;
#                 }
#             }
#         }
#         return res;
#     }
# };

# Java version:
# import java.util.*;
# class Solution {
#     public int uniquePathsIII(int[][] grid) {
#         int m = grid.length, n = grid[0].length;
#         int start_i = -1, start_j = -1, empty = 0;
#         for (int i = 0; i < m; ++i) {
#             for (int j = 0; j < n; ++j) {
#                 if (grid[i][j] == 1) {
#                     start_i = i; start_j = j;
#                 }
#                 if (grid[i][j] == 0) ++empty;
#             }
#         }
#         return backtrack(grid, start_i, start_j, empty);
#     }
#     private int backtrack(int[][] grid, int i, int j, int empty)
#     {
#         int m = grid.length, n = grid[0].length, res =
#             0;
#         int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};
#         for (int[] d : dirs) {
#             int x = i + d[0], y = j + d[1];
#             if (x >= 0 && x < m && y >= 0 && y < n) {
#                 if (grid[x][y] == 0) {
#                     grid[x][y] = -1;
#                     --empty;
#                     res += backtrack(grid, x, y, empty);
#                     grid[x][y] = 0;
#                     ++empty;
#                 } else if (grid[x][y] == 2) {
#                     res += empty == 0;
#                 }
#             }
#         }
#         return res;
#     }
# };