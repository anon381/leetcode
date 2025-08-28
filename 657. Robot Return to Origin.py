class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U")==moves.count("D") and moves.count("L")==moves.count("R")
# in java 
# class Solution {
#     public boolean judgeCircle(String moves) {
#         int x = 0, y = 0;

#         for(char move: moves.toCharArray()){
#             if(move == 'U') y++;
#             else if(move == 'D') y--;
#             else if(move == 'L') x--;
#             else if(move == 'R') x++;
#         }
#         return x == 0 && y == 0;
#     }
# }
