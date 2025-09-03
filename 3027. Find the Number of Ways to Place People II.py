class Solution:
    def numberOfPairs(self, P: List[List[int]]) -> int:
        P.sort(key=lambda p:(-p[0], p[1]))
        ans, n=0, len(P)
        for i in range(n-1):
            y, yi=1<<31, P[i][1]
            for j in range(i+1, n):
                yj=P[j][1]
                if y>yj>=yi:
                    ans+=1
                    y=yj
                    if yi==yj: break
        return ans
        
# in cpp
# class Solution {
# public:
#     static bool cmp(const vector<int>& p, const vector<int>& q){
#         return (p[0]==q[0])?p[1]<q[1]:p[0]>q[0];// order by (x, >)
#     }
#     static int numberOfPairs(vector<vector<int>>& P) {
#         sort(P.begin(), P.end(), cmp);
#         int n = P.size(), ans = 0;
#         for(int i=0; i<n-1; i++){
#             int y=INT_MAX, yi=P[i][1];
#             for(int j = i+1; j<n; j++){
#                 const int yj=P[j][1];
#                 if (yj>=yi && y>yj){//P[j] cannot be in between
#                     ans++;
#                     y=yj;
#                     if (yi==yj) break;
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
