class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1')
                    boxIndex = (i // 3) * 3 + (j // 3)
                    if rows[i][num] or cols[j][num] or boxes[boxIndex][num]:
                        return False
                    rows[i][num] = cols[j][num] = boxes[boxIndex][num] = True
        return True

        
# in cpp
# class Solution {
# public:
#     bool isValidSudoku(vector<vector<char>>& board) {
#         bool rows[9][9] = {false};
#         bool cols[9][9] = {false};
#         bool boxes[9][9] = {false};

#         for (int i = 0; i < 9; i++) {
#             for (int j = 0; j < 9; j++) {
#                 if (board[i][j] != '.') {
#                     int num = board[i][j] - '1';
#                     int boxIndex = (i / 3) * 3 + (j / 3);
#                     if (rows[i][num] || cols[j][num] || boxes[boxIndex][num]) return false;
#                     rows[i][num] = cols[j][num] = boxes[boxIndex][num] = true;
#                 }
#             }
#         }
#         return true;
#     }
# };



#in java 
# class Solution {
#     public boolean isValidSudoku(char[][] board) {
#         boolean[][] rows = new boolean[9][9];
#         boolean[][] cols = new boolean[9][9];
#         boolean[][] boxes = new boolean[9][9];

#         for (int i = 0; i < 9; i++) {
#             for (int j = 0; j < 9; j++) {
#                 if (board[i][j] != '.') {
#                     int num = board[i][j] - '1';
#                     int boxIndex = (i / 3) * 3 + (j / 3);

#                     if (rows[i][num] || cols[j][num] || boxes[boxIndex][num]) {
#                         return false;
#                     }

#                     rows[i][num] = cols[j][num] = boxes[boxIndex][num] = true;
#                 }
#             }
#         }
#         return true;
#     }
# }
