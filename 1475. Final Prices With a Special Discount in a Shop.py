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
