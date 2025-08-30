class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res[c][r] = matrix[r][c]
        
        return res



#in cpp
# class Solution {
# public:
#     vector<vector<int>> transpose(vector<vector<int>>& matrix) {
#         vector<vector<int>> res(matrix[0].size(), vector<int>(matrix.size(), 0));

#         for (size_t r = 0; r < matrix.size(); r++) {
#             for (size_t c = 0; c < matrix[0].size(); c++) {
#                 res[c][r] = matrix[r][c];
#             }
#         }

#         return res;        
#     }
# };
