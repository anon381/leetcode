Complexity
Time Complexity = 𝑂(𝑇⋅𝑚⋅𝑛 + 𝑇log⁡𝑇)
class Solution:

    def cutOffTree(self, forest: List[List[int]]) -> int:

        def bfs(beg, end):
            queue, uns = deque([(beg,0)]), unseen.copy()
            uns.discard(beg)

            while queue:
                (r,c), steps = queue.popleft()

                if (r,c) == end: return steps

                for R,C in ((r-1,c), (r,c-1), (r+1,c), (r,c+1)):

                    if (R,C) not in uns: continue

                    queue.append(((R,C),steps+1))
                    uns.discard((R,C))

            return -1
        
        m, n, ans = len(forest), len(forest[0]), 0
        start, trees = (0,0), []

        grid = tuple(product(range(m), range(n)))
        unseen = set(filter(lambda x: forest[x[0]][x[1]] != 0, grid))

        for r,c  in grid:
            if forest[r][c] > 1: heappush(trees,(forest[r][c], (r,c)))

        while trees:
            if (res:= bfs(start,(pos:= heappop(trees)[1]))) < 0: return -1

            ans += res
            start = pos

        return ans



#in cpp

#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int cutOffTree(vector<vector<int>>& forest) {
        int m = forest.size(), n = forest[0].size();
        vector<pair<int, pair<int,int>>> trees;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (forest[i][j] > 1) {
                    trees.push_back({forest[i][j], {i, j}});
                }
            }
        }
        sort(trees.begin(), trees.end());
        auto bfs = [&](pair<int,int> start, pair<int,int> end) -> int {
            if (start == end) return 0;
            queue<pair<int,int>> q;
            q.push(start);
            vector<vector<bool>> visited(m, vector<bool>(n, false));
            visited[start.first][start.second] = true;
            int steps = 0;
            vector<int> dirs = {0,1,0,-1,0};
            while (!q.empty()) {
                int sz = q.size();
                while (sz--) {
                    auto [r,c] = q.front(); q.pop();
                    if (make_pair(r,c) == end) return steps;
                    for (int k = 0; k < 4; k++) {
                        int R = r + dirs[k], C = c + dirs[k+1];
                        if (R >= 0 && R < m && C >= 0 && C < n && 
                            !visited[R][C] && forest[R][C] != 0) {
                            visited[R][C] = true;
                            q.push({R,C});
                        }
                    }
                }
                steps++;
            }
            return -1;
        };
        int ans = 0;
        pair<int,int> start = {0,0};
        for (auto& t : trees) {
            auto [height, pos] = t;
            int dist = bfs(start, pos);
            if (dist < 0) return -1;
            ans += dist;
            start = pos;
        }
        return ans;
    }
};















#in java
import java.util.*;

class Solution {
    public int cutOffTree(List<List<Integer>> forest) {
        int m = forest.size(), n = forest.get(0).size();
        List<int[]> trees = new ArrayList<>();

        // Collect all trees (value > 1)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int h = forest.get(i).get(j);
                if (h > 1) trees.add(new int[]{h, i, j});
            }
        }

        // Sort by height
        trees.sort(Comparator.comparingInt(a -> a[0]));

        int ans = 0;
        int[] start = {0, 0};

        for (int[] t : trees) {
            int[] target = {t[1], t[2]};
            int dist = bfs(forest, start, target);
            if (dist < 0) return -1;
            ans += dist;
            start = target;
        }
        return ans;
    }

    private int bfs(List<List<Integer>> forest, int[] start, int[] end) {
        if (start[0] == end[0] && start[1] == end[1]) return 0;

        int m = forest.size(), n = forest.get(0).size();
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> q = new LinkedList<>();
        q.add(start);
        visited[start[0]][start[1]] = true;

        int steps = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

        while (!q.isEmpty()) {
            int sz = q.size();
            while (sz-- > 0) {
                int[] cur = q.poll();
                int r = cur[0], c = cur[1];
                if (r == end[0] && c == end[1]) return steps;

                for (int[] d : dirs) {
                    int R = r + d[0], C = c + d[1];
                    if (R >= 0 && R < m && C >= 0 && C < n &&
                        !visited[R][C] && forest.get(R).get(C) != 0) {
                        visited[R][C] = true;
                        q.add(new int[]{R, C});
                    }
                }
            }
            steps++;
        }
        return -1;
    }
}
