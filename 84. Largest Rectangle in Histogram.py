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

        

#in java
# import java.util.Stack;

# class Solution {
#     public int largestRectangleArea(int[] heights) {
#         Stack<Integer> stack = new Stack<>();
#         stack.push(-1);
#         int maxArea = 0;

#         for (int i = 0; i < heights.length; i++) {
#             while (stack.peek() != -1 && heights[i] <= heights[stack.peek()]) {
#                 int height = heights[stack.pop()];
#                 int width = i - stack.peek() - 1;
#                 maxArea = Math.max(maxArea, height * width);
#             }
#             stack.push(i);
#         }

#         while (stack.peek() != -1) {
#             int height = heights[stack.pop()];
#             int width = heights.length - stack.peek() - 1;
#             maxArea = Math.max(maxArea, height * width);
#         }

#         return maxArea;
#     }
# }
