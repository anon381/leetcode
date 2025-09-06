# Complexity
# Time O(N)
# Space O(N)

class Solution:
    def finalPrices(self, A):
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] >= a:
                A[stack.pop()] -= a
            stack.append(i)
        return A        


#in c++
# class Solution {
# public:
#         vector<int> finalPrices(vector<int>& A) {
#         vector<int> stack;
#         for (int i = 0; i < A.size(); ++i) {
#             while (stack.size() && A[stack.back()] >= A[i]) {
#                 A[stack.back()] -= A[i];
#                 stack.pop_back();
#             }
#             stack.push_back(i);
#         }
#         return A;
#     }
# };




#in java
# class Solution {
#         public int[] finalPrices(int[] A) {
#         Stack<Integer> stack = new Stack<>();
#         for (int i = 0; i < A.length; i++) {
#             while (!stack.isEmpty() && A[stack.peek()] >= A[i])
#                 A[stack.pop()] -= A[i];
#             stack.push(i);
#         }
#         return A;
#     }
# }
