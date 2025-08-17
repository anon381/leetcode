

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        subtree_size = [1] * n
        distance_sum = [0] * n

        def dfs1(node, parent):
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs1(neighbor, node)
                    subtree_size[node] += subtree_size[neighbor]
                    distance_sum[node] += distance_sum[neighbor] + subtree_size[neighbor]

        def dfs2(node, parent):
            for neighbor in adj[node]:
                if neighbor != parent:
                    distance_sum[neighbor] = distance_sum[node] - subtree_size[neighbor] + (n - subtree_size[neighbor])
                    dfs2(neighbor, node)

        dfs1(0, -1)
        dfs2(0, -1)
        
        return distance_sum
