# Complexity 
# Time O(1) 
# Space O(1)

class Solution:
        def isBoomerang(self, p):
            return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])        




#c++ version
# class Solution {
# public:
#        bool isBoomerang(vector<vector<int>>& p) {
#         return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1]);
#     }
# };



# in java
# class Solution {
#         public boolean isBoomerang(int[][] p) {
#         return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1]);
#     }
# }
