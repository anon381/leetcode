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
