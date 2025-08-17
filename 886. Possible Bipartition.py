
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        A, B = 1, -1
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
        
        color = {}
        for i in range(1, N + 1):
            if i in color:
                continue
            color[i] = A
            queue = deque([(i, A)])
            
            while queue:
                node, c = queue.popleft()
                for nei in adj[node]:
                    if nei not in color:
                        color[nei] = -c
                        queue.append((nei, color[nei]))
                    elif color[nei] == c:
                        return False
        return True
