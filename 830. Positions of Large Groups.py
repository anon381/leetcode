class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        left = 0 
        return_list = []
        S += '1'
        for index, letter in enumerate(S):
            if letter != S[left]:
                if index - left >= 3:
                    return_list.append([left, index - 1])
                left = index
        return return_list


#in cpp
# class Solution {
# public:
#     vector<vector<int>> largeGroupPositions(string s) {
#         vector<vector<int>> res;
#         int start = 0;
#         for (int i = 1, n = s.length(); i <= n; ++i) {
#             if (i == n || s[i] != s[start]) {
#                 if (i - start >= 3) res.push_back({start, i - 1});
#                 start = i;
#             }
#         }
#         return res;
#     }
# };


#in java
# class Solution {
#     public List<List<Integer>> largeGroupPositions(String S) {
#         List<List<Integer>> ans = new ArrayList();
#         int i = 0, N = S.length(); // i is the start of each group
#         for (int j = 0; j < N; ++j) {
#             if (j == N-1 || S.charAt(j) != S.charAt(j+1)) {
#                 // Here, [i, j] represents a group.
#                 if (j-i+1 >= 3)
#                     ans.add(Arrays.asList(new Integer[]{i, j}));
#                 i = j + 1;
#             }
#         }

#         return ans;
#     }
# }
