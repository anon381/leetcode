class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        import heapq
        n, m = len(grid), len(grid[0])
        diags = {}

        for i in range(n):
            for j in range(m):
                key = i - j
                if key not in diags: diags[key] = []
                if key < 0: heapq.heappush(diags[key], grid[i][j])
                else: heapq.heappush(diags[key], -grid[i][j])

        for i in range(n):
            for j in range(m):
                key = i - j
                if key < 0: grid[i][j] = heapq.heappop(diags[key])
                else: grid[i][j] = -heapq.heappop(diags[key])
        return grid
# in cpp
# class Solution {
# public:
#     vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
#         int n = grid.size(), m = grid[0].size();
#         unordered_map<int, priority_queue<int>> maxHeaps;
#         unordered_map<int, priority_queue<int, vector<int>, greater<int>>> minHeaps;

#         for (int i = 0; i < n; i++) {
#             for (int j = 0; j < m; j++) {
#                 int key = i - j;
#                 if (key < 0) minHeaps[key].push(grid[i][j]);
#                 else maxHeaps[key].push(grid[i][j]);
#             }
#         }

#         for (int i = 0; i < n; i++) {
#             for (int j = 0; j < m; j++) {
#                 int key = i - j;
#                 if (key < 0) {
#                     grid[i][j] = minHeaps[key].top();
#                     minHeaps[key].pop();
#                 } else {
#                     grid[i][j] = maxHeaps[key].top();
#                     maxHeaps[key].pop();
#                 }
#             }
#         }
#         return grid;
#     }
# };
