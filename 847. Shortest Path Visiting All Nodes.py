# Time Complexity: O(N^2 * 2^N), where N is the number of nodes in the graph
# Space Complexity: O(N * 2^N), for the queue and visited set
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(1 << i, i, 0) for i in range(n)])
        visited = set((1 << i, i) for i in range(n))
        
        while queue:
            mask, node, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))

# Function Description:
# This function finds the shortest path that visits all nodes in an undirected graph.
# It uses a breadth-first search (BFS) approach, where each state is represented by a bitmask
# indicating which nodes have been visited, the current node, and the current path length.
# The queue stores all possible states, and the visited set ensures that each state is processed only once.
# The algorithm starts BFS from every node, and the search continues until all nodes have been visited
# (i.e., the bitmask has all bits set). The function returns the minimum number of steps required to visit all nodes.


# in cpp
# class Solution {
# public:
#     int shortestPathLength(vector<vector<int>>& graph) {
#         int n = graph.size();
#         queue<tuple<int, int, int>> q;
#         for (int i = 0; i < n; i++) {
#             q.push({1 << i, i, 0});
#         }
#         set<pair<int, int>> visited;
#         while (!q.empty()) {
#             auto [mask, node, dist] = q.front();
#             q.pop();
#             if (mask == (1 << n) - 1) {
#                 return dist;
#             }
#             for (int neighbor : graph[node]) {
#                 int new_mask = mask | (1 << neighbor);
#                 if (visited.find({new_mask, neighbor}) == visited.end()) {
#                     visited.insert({new_mask, neighbor});
#                     q.push({new_mask, neighbor, dist + 1});
#                 }
#             }
#         }
#         return -1;
#     }
# };


# in java
# import java.util.*;
# class Solution {
#     public int shortestPathLength(int[][] graph) {
#         int n = graph.length;
#         Queue<int[]> queue = new LinkedList<>();
#         for (int i = 0; i < n; i++) {
#             queue.offer(new int[]{1 << i, i, 0});
#         }
#         Set<String> visited = new HashSet<>();
#         while (!queue.isEmpty()) {
#             int[] curr = queue.poll();
#             int mask = curr[0], node = curr[1], dist = curr[2];
#             if (mask == (1 << n) - 1) {
#                 return dist;
#             }
#             for (int neighbor : graph[node]) {
#                 int new_mask = mask | (1 << neighbor);
#                 String state = new_mask + "," + neighbor;
#                 if (!visited.contains(state)) {
#                     visited.add(state);
#                     queue.offer(new int[]{new_mask, neighbor, dist + 1});
#                 }
#             }
#         }
#         return -1;
#     }
# };
