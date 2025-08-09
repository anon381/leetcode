class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        perimeter = 0

        def dfs(x, y):
            nonlocal perimeter
            grid[x][y] = -1  # Mark as visited
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx < 0 or ny < 0 or nx == rows or ny == cols or grid[nx][ny] == 0):
                    perimeter += 1
                elif grid[nx][ny] == 1:
                    dfs(nx, ny)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter  

        return 0
