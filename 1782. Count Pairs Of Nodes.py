class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:


        degs = [0]*n
        count = {}
        for u, v in edges:
            u -= 1
            v -= 1

            u, v = min(u, v), max(u, v)

            degs[u] += 1
            degs[v] += 1
            count[(u, v)] = count.get((u, v), 0) + 1



        out = []
        ordered = degs[:]
        ordered.sort()
        
        for q in queries:
            pairs = 0
            j = n-1
            for i in range(n):
                di = ordered[i]
                while j >= 0 and di + ordered[j] > q: j -= 1
                pairs += n-1-j
                if j < i: pairs -= 1 

            pairs //= 2 

            for (u, v), c in count.items():
                if degs[u] + degs[v] > q and degs[u]+degs[v]-c <= q: 
                    pairs -= 1

            out.append(pairs)

        return out
