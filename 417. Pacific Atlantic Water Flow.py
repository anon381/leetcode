Time complexity:
O(m×n)

from collections import deque
class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            reachable = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and 0 <= nc < n and
                        (nr, nc) not in reachable and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        reachable.add((nr, nc))
                        q.append((nr, nc))
            return reachable

        pacific_starts = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        atlantic_starts = [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m)]

        pacific_reach = bfs(pacific_starts)
        atlantic_reach = bfs(atlantic_starts)

        return list(map(list, pacific_reach & atlantic_reach))
