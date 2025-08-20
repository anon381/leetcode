
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] = min(
                        matrix[i-1][j],
                        matrix[i][j-1],
                        matrix[i-1][j-1]
                    ) + 1
                res += matrix[i][j]

        return res
## or 
class Solution:
    def countSquares(self, grid: List[List[int]]) -> int:
        ans=0
        r=len(grid)
        c=len(grid[0])
        maxx=0
        for dig in range(c):
            ans += grid[0][dig]
        for dig in range(1,r):
            ans += grid[dig][0]
        for i in range(1,r):
            for j in range(1,c):
                if grid[i][j] == 1 and grid[i][j-1] > 0 and grid[i-1][j] > 0 and grid[i-1][j-1] > 0:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1],grid[i-1][j-1])
                ans += grid[i][j]
        return ans
