class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        users = defaultdict(set)
        for u, t in logs:
            users[u].add(t)
        answer = [0]*k
        for s in users.values():
            u = len(s)
            if u <= k:
                answer[u-1] += 1
        return answer


#in cpp
# class Solution {
# public:
#     vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
#         unordered_map<int,unordered_set<int>>m;
#         for(int i=0 ; i<logs.size() ; i++)
#         {
#             m[logs[i][0]].insert(logs[i][1]);
#         }
#         vector<int>UAM;
        
#         for(auto it : m)
#         {
#             UAM.push_back(it.second.size());
#         }
#         vector<int>result(k,0);
#         for(int i = 0; i < UAM.size(); i++) {
#         int uam_count = UAM[i];
#         if(uam_count <= k) {  // boundary check
#         result[uam_count - 1]++;
#         }
#     }
#     return result;

#     }
# };
