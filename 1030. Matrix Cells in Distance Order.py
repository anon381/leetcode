class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        bfsQ = deque([[rCenter, cCenter]])
        result = []
        visited = [[False] * cols for _ in range(rows)]
        visited[rCenter][cCenter] = True
        dirs = [(0, +1), (0, -1), (+1, 0), (-1, 0)]

        while bfsQ:
            cell = bfsQ.popleft()
            result.append(cell)
            for delta in dirs:
                r = cell[0] + delta[0]
                c = cell[1] + delta[1]
                if r >= 0 and r < rows and c >= 0 and c < cols and not visited[r][c]:
                    visited[r][c] = True
                    bfsQ.append([r, c])
        return result
