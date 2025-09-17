class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter = coordinates[0]
        num = coordinates[1]
        if ord(letter) % 2 == 0:
            return int(num) % 2 != 0
        else:
            return int(num) % 2 == 0


#in cpp
# class Solution {
# public:
#     bool squareIsWhite(string coordinates) {
#         char letter = coordinates[0];
#         char num = coordinates[1];
        
#         if (letter % 2 == 0) {
#             return (num - '0') % 2 != 0;
#         } else {
#             return (num - '0') % 2 == 0;
#         }
#     }
# };


#in java
