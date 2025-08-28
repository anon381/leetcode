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


# in cpp
# class Solution {
# public:
#     bool judgeCircle(string moves) {
#         int cntR=0;int cntL=0;int cntU=0;int cntD=0;
#         for(int i=0;i<moves.size();i++){
#          if(moves[i]=='L') cntL++;
#          if(moves[i]=='R') cntR++;
#          if(moves[i]=='U') cntU++;
#          if(moves[i]=='D') cntD++;
#         }
#         if(cntL==cntR && cntU==cntD) return true;
#         return false;
#     }
# };
