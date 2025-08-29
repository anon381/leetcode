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
