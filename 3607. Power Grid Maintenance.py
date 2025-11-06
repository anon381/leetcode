class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))
        size = [1] * (c + 1)
        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def unite(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
        for u, v in connections:
            unite(u, v)
        heaps = {}
        for i in range(1, c + 1):
            r = find(i)
            if r not in heaps:
                heaps[r] = []
            heaps[r].append(i)
        for r in heaps:
            heapq.heapify(heaps[r])
        offline = [False] * (c + 1)
        ans = []
        for t, x in queries:
            if t == 2:
                offline[x] = True
            else:
                if not offline[x]:
                    ans.append(x)
                else:
                    r = find(x)
                    h = heaps.get(r, [])
                    while h and offline[h[0]]:
                        heapq.heappop(h)
                    ans.append(h[0] if h else -1)
        return ans

#in cpp
class Solution {
public:
    struct DSU {
        vector<int> p, sz;
        DSU(int n=0): p(n+1), sz(n+1,1){
            iota(p.begin(), p.end(), 0);
        }
        int find(int x){ return p[x]==x? x : p[x]=find(p[x]); }
        void unite(int a, int b){
            a = find(a); b = find(b);
            if(a==b) return;
            if(sz[a] < sz[b]) swap(a,b);
            p[b]=a; sz[a]+=sz[b];
        }
    };

    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        DSU dsu(c);
        for (auto &e : connections) dsu.unite(e[0], e[1]);

        unordered_map<int, priority_queue<int, vector<int>, greater<int>>> heap;
        heap.reserve(c*2);

        for (int i = 1; i <= c; ++i) {
            int r = dsu.find(i);
            heap[r].push(i);
        }

        vector<char> offline(c+1, false);
        vector<int> ans;
        ans.reserve(queries.size());

        for (auto &q : queries) {
            int t = q[0], x = q[1];
            if (t == 2) {
                offline[x] = true;
            } else {
                if (!offline[x]) {
                    ans.push_back(x);
                } else {
                    int r = dsu.find(x);
                    auto &pq = heap[r];
                    while (!pq.empty() && offline[pq.top()]) pq.pop();
                    if (pq.empty()) ans.push_back(-1);
                    else ans.push_back(pq.top());
                }
            }
        }
        return ans;
    }
};



#in java
import java.util.*;

class Solution {
    static class DSU {
        int[] p, sz;
        DSU(int n){
            p = new int[n+1];
            sz = new int[n+1];
            for (int i = 0; i <= n; i++){ p[i]=i; sz[i]=1; }
        }
        int find(int x){ return p[x]==x? x : (p[x]=find(p[x])); }
        void unite(int a, int b){
            a = find(a); b = find(b);
            if(a==b) return;
            if(sz[a] < sz[b]) { int tmp=a; a=b; b=tmp; }
            p[b]=a; sz[a]+=sz[b];
        }
    }

    public int[] processQueries(int c, int[][] connections, int[][] queries) {
        DSU dsu = new DSU(c);
        for (int[] e : connections) dsu.unite(e[0], e[1]);

        Map<Integer, PriorityQueue<Integer>> heap = new HashMap<>();
        for (int i = 1; i <= c; i++) {
            int r = dsu.find(i);
            heap.computeIfAbsent(r, k -> new PriorityQueue<>()).offer(i);
        }

        boolean[] offline = new boolean[c+1];
        List<Integer> res = new ArrayList<>(queries.length);

        for (int[] q : queries) {
            int t = q[0], x = q[1];
            if (t == 2) {
                offline[x] = true;
            } else {
                if (!offline[x]) {
                    res.add(x);
                } else {
                    int r = dsu.find(x);
                    PriorityQueue<Integer> pq = heap.get(r);
                    if (pq == null) { res.add(-1); continue; }
                    while (!pq.isEmpty() && offline[pq.peek()]) pq.poll();
                    res.add(pq.isEmpty() ? -1 : pq.peek());
                }
            }
        }

        int[] ans = new int[res.size()];
        for (int i = 0; i < res.size(); i++) ans[i] = res.get(i);
        return ans;
    }
}
