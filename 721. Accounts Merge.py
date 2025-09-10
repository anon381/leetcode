"""
Time Complexity: O(N * K), where N is the number of accounts and K is the average number of emails per account
"""
"""
Space Complexity: O(N * K), for storing all accounts and emails in data structures
"""
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
        
    # Description:
    # This solution merges accounts by grouping emails that belong to the same person.
    # It uses sets to track emails for each name and merges overlapping sets when common emails are found.
    # The result is a list of accounts with merged emails, sorted for each person.

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

# Java version of the above Python code:
# import java.util.*;
# class Solution {
#     public List<List<String>> accountsMerge(List<List<String>> accounts) {
#         Map<String, String> emailToName = new HashMap<>();
#         Map<String, Set<String>> graph = new HashMap<>();
#         for (List<String> account : accounts) {
#             String name = account.get(0);
#             for (int i = 1; i < account.size(); i++) {
#                 String email = account.get(i);
#                 emailToName.put(email, name);
#                 graph.putIfAbsent(email, new HashSet<>());
#                 if (i > 1) {
#                     graph.get(account.get(i - 1)).add(email);
#                     graph.get(email).add(account.get(i - 1));
#                 }
#             }
#         }
#
#         Set<String> visited = new HashSet<>();
#         List<List<String>> mergedAccounts = new ArrayList<>();
#         for (String email : emailToName.keySet()) {
#             if (!visited.contains(email)) {
#                 List<String> merged = new ArrayList<>();
#                 dfs(email, visited, graph, merged);
#                 Collections.sort(merged);
#                 mergedAccounts.add(new ArrayList<>(Arrays.asList(emailToName.get(email))));
#                 mergedAccounts.get(mergedAccounts.size() - 1).addAll(merged);
#             }
#         }
#         return mergedAccounts;
#     }
#
#     private void dfs(String email, Set<String> visited,
#                      Map<String, Set<String>> graph,
#                      List<String> merged) {
#         visited.add(email);
#         merged.add(email);
#         for (String neighbor : graph.get(email)) {
#             if (!visited.contains(neighbor)) {
#                 dfs(neighbor, visited, graph, merged);
#             }
#         }
#     }
# };
