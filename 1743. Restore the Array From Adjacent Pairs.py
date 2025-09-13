
class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        # Create a graph to represent adjacent pairs
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize the result list
        res = []

        # Find the starting node with only one neighbor
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                res = [node, neighbors[0]]
                break

        # Continue building the array until its length matches the number of pairs
        while len(res) < len(pairs) + 1:
            # Get the last two elements in the result array
            last, prev = res[-1], res[-2]

            # Find the candidates for the next element
            candidates = graph[last]

            # Choose the candidate that is not the previous element
            next_element = candidates[0] if candidates[0] != prev else candidates[1]

            # Append the next element to the result array
            res.append(next_element)

        return res


#in cpp

# class Solution {
# public:
#     vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
#         unordered_map<int, vector<int>> graph;

#         for (const auto& pair : adjacentPairs) {
#             graph[pair[0]].push_back(pair[1]);
#             graph[pair[1]].push_back(pair[0]);
#         }

#         vector<int> result;

#         for (const auto& entry : graph) {
#             if (entry.second.size() == 1) {
#                 result = {entry.first, entry.second[0]};
#                 break;
#             }
#         }

#         while (result.size() < adjacentPairs.size() + 1) {
#             int last = result[result.size() - 1];
#             int prev = result[result.size() - 2];
#             const vector<int>& candidates = graph[last];
#             int nextElement = (candidates[0] != prev) ? candidates[0] : candidates[1];
#             result.push_back(nextElement);
#         }

#         return result;        
#     }
# };
