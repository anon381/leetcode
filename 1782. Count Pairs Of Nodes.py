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


#in cpp

# class Solution {
# public:
#     vector<int> countPairs(int n, vector<vector<int>>& edges, vector<int>& queries) {
#         vector<int> degree(n+1,0);
#         map<pair<int,int>, int> shared;
#         for(auto &edge : edges) {
#             degree[edge[0]]++;
#             degree[edge[1]]++;
#             shared[{min(edge[0],edge[1]),max(edge[0],edge[1])}]++;
#         }
#         vector<int> original = degree;
        
#         sort(degree.begin(),degree.end());
#         vector<int> answers;
#         for(auto &q : queries) {
#             int l = 1,r = n;
#             long long ans= 0;
#             while(l < r) {
             
#                 if(degree[l] + degree[r] > q) {
                    
#                     ans += (r - l);
                    
#                     r--;
#                 }
#                 else l++;
#             }
            

#             for(auto &[key,val] : shared) {
    
#                 if((original[key.first] + original[key.second] > q) && (original[key.first] + original[key.second] - val <= q)) {
#                     ans--;
#                 }
#             }
#             answers.push_back(ans);
#         }
#         return answers;
#     }
# };
