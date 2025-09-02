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
