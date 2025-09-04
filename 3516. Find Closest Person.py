class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a, b = abs(x - z), abs(y - z)
        return (a != b) << (a > b)

        
# C++ version
# class Solution {
# public:
#     int findClosest(int x, int y, int z) {
#         int a = abs(x - z), b = abs(y - z);
#         return (a != b) << (a > b);
#     }
# };


# java version 
# class Solution {
#     public int findClosest(int x, int y, int z) {
#         int a = Math.abs(x - z), b = Math.abs(y - z);
#         return ((a > b) ? 2 : 0) | ((a < b) ? 1 : 0);
#     }
# }
