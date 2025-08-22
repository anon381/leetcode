class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minRow, maxRow = m, -1
        minCol, maxCol = n, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    minRow = min(minRow, i)
                    maxRow = max(maxRow, i)
                    minCol = min(minCol, j)
                    maxCol = max(maxCol, j)

        return (maxRow - minRow + 1) * (maxCol - minCol + 1)
## or, a bit different approach.

class Solution(object):
    def minimumArea(self, grid):
        r=len(grid)
        c=len(grid[0])
        rs=rl=-1
        cs=cl=-1
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    if rs==-1:
                        rs=i
                    rl=i
                    if cs==-1:
                        cs=j
                    else:
                        cs=min(cs,j)
                    cl=max(cl,j)
        b=(rl-rs)+1
        l=(cl-cs)+1
        return b*l
