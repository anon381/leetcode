
# Sorting	O(n log n)	O(1)
# Pair sweeping	O(n²)	O(1)
# Total	O(n²)	O(1)

class Solution:
    def numberOfPairs(self, P: List[List[int]]) -> int:
        P.sort(key=lambda p: (-p[0], p[1]))
        n, ans=len(P), 0
        for i in range(n-1):
            y=1<<31
            for j in range(i+1, n):
                if y>P[j][1]>=P[i][1]:
                    ans+=1
                    y=P[j][1]
        return ans




#in cpp
# class Solution {
# public:
#     static bool cmp(vector<int>& p, vector<int>& q){
#         return (p[0]==q[0])?p[1]<q[1]:p[0]>q[0];
#     }

#     int numberOfPairs(vector<vector<int>>& P) {
#         sort(P.begin(), P.end(), cmp);
#         int n = P.size(), ans = 0;
#         for(int i=0; i<n-1; i++){
#             int y=INT_MAX;
#             for(int j = i+1; j<n; j++){
#                 if (P[j][1]>=P[i][1] && y>P[j][1]){
#                     ans++;
#                     y=P[j][1];
#                 }
#             }
#         }
#         return ans;
#     }
# };

# auto init = []()
# { 
#     ios::sync_with_stdio(0);
#     cin.tie(0);
#     cout.tie(0);
#     return 'c';
# }();
