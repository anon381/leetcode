class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))) for [x1,y1], [x2,y2], [x3,y3] in combinations(points, 3))
# or in cpp
# #include <bits/stdc++.h>
# using namespace std;

# class Solution {
# public:
#     double largestTriangleArea(vector<vector<int>>& points) {
#         double maxArea = 0.0;
#         int n = points.size();
        
#         for (int i = 0; i < n; i++) {
#             for (int j = i + 1; j < n; j++) {
#                 for (int k = j + 1; k < n; k++) {
#                     double x1 = points[i][0], y1 = points[i][1];
#                     double x2 = points[j][0], y2 = points[j][1];
#                     double x3 = points[k][0], y3 = points[k][1];
                    
#                     double area = fabs(0.5 * (x1 * (y2 - y3) +
#                                               x2 * (y3 - y1) +
#                                               x3 * (y1 - y2)));
#                     maxArea = max(maxArea, area);
#                 }
#             }
#         }
#         return maxArea;
#     }
# };
