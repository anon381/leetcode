class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        return not (
            rec1[2] <= rec2[0] or  
            rec1[0] >= rec2[2] or  
            rec1[3] <= rec2[1] or  
            rec1[1] >= rec2[3]    
        )
# or in cpp
# #include <bits/stdc++.h>
# using namespace std;

# class Solution {
# public:
#     bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
#         return !(
#             rec1[2] <= rec2[0] ||  // left
#             rec1[0] >= rec2[2] ||  // right
#             rec1[3] <= rec2[1] ||  // bottom
#             rec1[1] >= rec2[3]     // top
#         );
#     }
# };
