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



#in cpp
# class Solution {
# public:
#     vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
#         queue<vector<int>> bfsQ;
#         bfsQ.push({rCenter, cCenter});
#         vector<vector<int>> result;
#         vector<vector<bool>> visited(rows, vector<bool>(cols));
#         visited[rCenter][cCenter] = true;
#         const vector<vector<int>> dirs = {{0, +1}, {0, -1}, {+1, 0}, {-1, 0}};

#         while (bfsQ.size()) {
#             vector<int> cell = bfsQ.front();
#             bfsQ.pop();
#             result.push_back(cell);
#             for (vector<int> deltas : dirs) {
#                 int r = cell[0] + deltas[0];
#                 int c = cell[1] + deltas[1];
#                 if (r >= 0 && r < rows && c >= 0 && c < cols &&
#                     !visited[r][c]) {
#                     visited[r][c] = true;
#                     bfsQ.push({r, c});
#                 }
#             }
#         }
#         return result;
#     }
# };




#in java
# class Solution {
#     public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
#         Queue<int[]> bfsQ = new LinkedList();
#         int[][] result = new int[rows * cols][];
#         int resultIdx = 0;
#         bfsQ.add(new int[] { rCenter, cCenter });
#         boolean[][] visited = new boolean[rows][cols];
#         visited[rCenter][cCenter] = true;
#         final int[][] dirs = { { 0, +1 }, { 0, -1 }, { +1, 0 }, { -1, 0 } };

#         while (!bfsQ.isEmpty()) {
#             int[] cell = bfsQ.poll();
#             result[resultIdx++] = cell;
#             for (int[] deltas : dirs) {
#                 int r = cell[0] + deltas[0];
#                 int c = cell[1] + deltas[1];
#                 if (r >= 0 && r < rows && c >= 0 && c < cols && !visited[r][c]) {
#                     visited[r][c] = true;
#                     bfsQ.add(new int[] { r, c });
#                 }
#             }
#         }
#         return result;
#     }
# }

