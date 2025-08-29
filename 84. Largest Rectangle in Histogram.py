class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area


#in cpp
# class Solution {
# public:
#     int largestRectangleArea(vector<int>& heights) {
#         stack<int> stack;
#         stack.push(-1);
#         int max_area = 0;

#         for (int i = 0; i < heights.size(); i++) {
#             while (stack.top() != -1 && heights[i] <= heights[stack.top()]) {
#                 int height = heights[stack.top()];
#                 stack.pop();
#                 int width = i - stack.top() - 1;
#                 max_area = max(max_area, height * width);
#             }
#             stack.push(i);
#         }

#         while (stack.top() != -1) {
#             int height = heights[stack.top()];
#             stack.pop();
#             int width = heights.size() - stack.top() - 1;
#             max_area = max(max_area, height * width);
#         }

#         return max_area;        
#     }
# };
