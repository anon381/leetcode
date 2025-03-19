# Time Complexity: O(4^k), where k is the number of empty squares
# Space Complexity: O(k), for recursion stack and grid modifications
class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
         # Get grid dimensions
        start = None  
        # Will hold the starting position
        count = 0 
         # Count of empty squares to visit
        for i in range(m): 
             # Iterate over each row
            for j in range(n):  
                # Iterate over each column
                count += grid[i][j] == 0  
                # Increment count if cell is empty
                if not start and grid[i][j] == 1: 
                     # If cell is the start
                    start = (i, j) 
                     # Save starting position

        def backtrack(i: int, j: int) -> int:
            nonlocal count  
            # Use the outer count variable
            result = 0 
             # Number of valid paths from this cell
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):  # Explore all 4 directions
                if 0 <= x < m and 0 <= y < n: 
                     # Check bounds
                    if grid[x][y] == 0: 
                         # If cell is empty
                        grid[x][y] = -1 
                         # Mark cell as visited
                        count -= 1  
                        # Decrement empty count
                        result += backtrack(x, y)  
                        # Recurse to next cell
                        grid[x][y] = 0  
                        # Unmark cell (backtrack)
                        count += 1  
                        # Restore empty count
                    elif grid[x][y] == 2: 
                         # If cell is the end
                        result += count == 0  
                        # Valid path only if all empty cells visited
            return result  
            # Return number of valid paths from this cell
        return backtrack(start[0], start[1])  
        # Start backtracking from the start position




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