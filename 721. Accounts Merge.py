from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        sol = defaultdict(list)
        for a in accounts:
            name = a[0]
            cur_emails = set(a[1:])
            if name not in sol:
                sol[name]=[cur_emails]
            else:
                merged=False
                newsets=[]
                for cur_set in sol[name]:
                    if len(cur_set.intersection(cur_emails)):
                        cur_emails.update(cur_set)
                        merged=True
                    else:
                        newsets.append(cur_set)
                if not merged:
                    sol[name].append(cur_emails)
                else:
                    newsets.append(cur_emails)
                    sol[name]=newsets
        output =[]
        for k in sol.keys():
            inner = sol[k]
            for cur_set in inner:
                output.append([k]+sorted(list(cur_set)))
        return output
        

# C++ version of the above Python code:
# #include <vector>
# #include <string>
# #include <unordered_map>
# #include <unordered_set>
# using namespace std;
#
# class Solution {
# public:
#     vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
#         unordered_map<string, unordered_set<string>> email_to_name;
#         unordered_map<string, unordered_set<string>> graph;
#         for (const auto& account : accounts) {
#             const string& name = account[0];
#             for (int i = 1; i < account.size(); ++i) {
#                 const string& email = account[i];
#                 email_to_name[email] = name;
#                 graph[email];  // Ensure the email is in the graph
#                 if (i > 1) {
#                     graph[account[i - 1]].insert(email);
#                     graph[email].insert(account[i - 1]);
#                 }
#             }
#         }
#
#         unordered_set<string> visited;
#         vector<vector<string>> merged_accounts;
#         for (const auto& [email, name] : email_to_name) {
#             if (!visited.count(email)) {
#                 vector<string> merged;
#                 dfs(email, visited, graph, merged);
#                 sort(merged.begin(), merged.end());
#                 merged_accounts.push_back({name});
#                 merged_accounts.back().insert(merged_accounts.back().end(), merged.begin(), merged.end());
#             }
#         }
#         return merged_accounts;
#     }
#
# private:
#     void dfs(const string& email, unordered_set<string>& visited,
#              const unordered_map<string, unordered_set<string>>& graph,
#              vector<string>& merged) {
#         visited.insert(email);
#         merged.push_back(email);
#         for (const string& neighbor : graph.at(email)) {
#             if (!visited.count(neighbor)) {
#                 dfs(neighbor, visited, graph, merged);
#             }
#         }
#     }
# };