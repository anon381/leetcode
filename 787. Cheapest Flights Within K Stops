class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj={i:[] for i in range(n)}
        for u,v,w in flights:
            adj[u].append((v,w))
        dist=[float('inf')]*n
        dist[src]=0
        q=[]
        heapq.heappush(q,(0, src, 0))
        while q:
            stops,node,wei=heapq.heappop(q)
            if stops>k:
                continue
            for nei,w in adj[node]:
                if dist[nei]>wei+w and stops<=k:
                    dist[nei]=wei+w
                    heapq.heappush(q,((stops+1,nei,wei+w)))
        print(dist)
        if dist[dst]==float('inf'):
            return -1
        return dist[dst]
