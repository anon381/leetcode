from collections import deque
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
      if not matrix or not matrix[0]:
            return False                
        expected = deque(matrix[0])
        for row_i in range(1, len(matrix)):
            row = matrix[row_i]
            expected.pop()
            expected.appendleft(row[0])
            for col_i in range(1, len(row)):
                if row[col_i] != expected[col_i]:
                    return False
        return True
#or in cpp
# class Solution {
# public:
#        bool isToeplitzMatrix(vector<vector<int>>& matrix) {
#     int n = matrix.size(), m = matrix[0].size();
#     map<int, int> mp;
#     for (int i = 0; i < n; i++) {
#         for (int j = 0; j < m; j++) {
#             if (mp.count(i - j) == 0)
#                 mp[i - j] = matrix[i][j];
#             else if (mp[i - j] != matrix[i][j])
#                 return 0;
#         }
#     }
#     return 1;
# } 
    
# };
