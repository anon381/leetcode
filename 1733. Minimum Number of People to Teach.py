"""
Time Complexity: O(n * m + f), where n is the number of languages, m is the number of people, and f is the number of friendships
"""
"""
Space Complexity: O(m + f), for storing knowledge sets and friendship pairs
"""

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)  # Number of people
        know = [set() for _ in range(m)]  # List of sets of languages known by each person
        for i, L in enumerate(languages):  # For each person
            know[i] = set(L)  # Store the set of languages they know

        need = set()  # Set of people who need to be taught
        for a1, b1 in friendships:  # For each friendship
            a, b = a1 - 1, b1 - 1  # Convert to 0-based index
            if know[a] & know[b]:  # If they share a language
                continue  # No need to teach
            need.add(a)  # Otherwise, add both to need set
            need.add(b)

        if not need:
            return 0  # If everyone can communicate, return 0

        ans = float('inf')  # Initialize answer to infinity
        for lang in range(1, n + 1):  # For each language
            cnt = 0  # Count of people to teach this language
            for i in need:  # For each person who needs to be taught
                if lang not in know[i]:  # If they don't know this language
                    cnt += 1  # Increment count
            ans = min(ans, cnt)  # Update answer if smaller
        return ans  # Return the minimum number of people to teach
        
    # Description:
    # This solution determines the minimum number of people that need to be taught a new language so that all friendships can communicate.
    # It first builds sets of languages known by each person, then identifies which friendships cannot communicate.
    # For each language, it counts how many people in the problematic friendships do not know that language, and finds the minimum such count.
    # The answer is the smallest number of people to teach a single language so all friendships are covered.

# C++ version of the above Python code:
# #include <vector>
# #include <set>
# using namespace std;
#
# class Solution {
# public:
#     int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
#         int m = languages.size();
#         vector<set<int>> know(m);
#         for (int i = 0; i < m; i++) {
#             know[i] = set<int>(languages[i].begin(), languages[i].end());
#         }
#
#         set<int> need;
#         for (auto& f : friendships) {
#             int a = f[0] - 1, b = f[1] - 1;
#             if (!know[a].empty() && !know[b].empty() && !set_intersection(know[a].begin(), know[a].end(), know[b].begin(), know[b].end())) {
#                 need.insert(a);
#                 need.insert(b);
#             }
#         }
#
#         if (need.empty()) return 0;
#
#         int ans = INT_MAX;
#         for (int lang = 1; lang <= n; lang++) {
#             int cnt = 0;
#             for (int i : need) {
#                 if (know[i].find(lang) == know[i].end()) cnt++;
#             }
#             ans = min(ans, cnt);
#         }
#         return ans;
#     }
# };

# Java version of the above Python code:
# import java.util.*;
# class Solution {
#     public int minimumTeachings(int n, List<List<Integer>> languages, List<List<Integer>> friendships) {
#         int m = languages.size();
#         List<Set<Integer>> know = new ArrayList<>();
#         for (int i = 0; i < m; i++) {
#             know.add(new HashSet<>(languages.get(i)));
#         }
#
#         Set<Integer> need = new HashSet<>();
#         for (List<Integer> f : friendships) {
#             int a = f.get(0) - 1, b = f.get(1) - 1;
#             if (!know.get(a).isEmpty() && !know.get(b).isEmpty() && Collections.disjoint(know.get(a), know.get(b))) {
#                 need.add(a);
#                 need.add(b);
#             }
#         }
#
#         if (need.isEmpty()) return 0;
#
#         int ans = Integer.MAX_VALUE;
#         for (int lang = 1; lang <= n; lang++) {
#             int cnt = 0;
#             for (int i : need) {
#                 if (!know.get(i).contains(lang)) cnt++;
#             }
#             ans = Math.min(ans, cnt);
#         }
#         return ans;
#     }
# };
