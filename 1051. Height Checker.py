class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


#in cpp
# class Solution {
# public:
#     int heightChecker(vector<int>& heights) {
#         vector<int> v(heights);
#         sort(v.begin(),v.end());
#         int count = 0;
#         for(int i=0;i<heights.size();i++){
#             if(heights[i] != v[i])
#              count++;
#         }
#         return count;
#     }
# };


#in java
# class Solution {
#     public int heightChecker(int[] heights) {
#         int[] expected = heights.clone();
#         Arrays.sort(expected);
#         int count = 0;
#         for (int i = 0; i < heights.length; i++) {
#             if (heights[i] != expected[i])
#                 count++;
#         }
#         return count;
#     }
# }
