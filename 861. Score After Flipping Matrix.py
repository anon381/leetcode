
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = (1 << (N - 1)) * M
        for j in range(1, N):
            cur = sum(grid[i][j] == grid[i][0] for i in range(M))
            res += max(cur, M - cur) * (1 << (N - 1 - j))
        return res


#in cpp
    int matrixScore(vector<vector<int>> A) {
        int M = A.size(), N = A[0].size(), res = (1 << (N - 1)) * M;
        for (int j = 1; j < N; j++) {
            int cur = 0;
            for (int i = 0; i < M; i++) cur += A[i][j] == A[i][0];
            res += max(cur, M - cur) * (1 << (N - j - 1));
        }
        return res;
    }
