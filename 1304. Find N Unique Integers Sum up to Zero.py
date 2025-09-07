# Complexity
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ n * (1 - n) // 2] + list(range(1, n))

# or

class Solution(object):
    def sumZero(self, n):
        return range(1 - n, n, 2)

#in cpp
# class Solution {
# public:
#     vector<int> sumZero(int n) {
#         vector<int> res(n);
#         res[0] = n * (1 - n) / 2;
#         for (int i = 1; i < n; ++i)
#             res[i] = i;
#         return res;
#     }
# };


        
#in java
# class Solution {
#     public int[] sumZero(int n) {
#         int[] res = new int[n];
#         res[0] = n * (1 - n) / 2;
#         for (int i = 1; i < n; ++i)
#             res[i] = i;
#         return res;
#     }
# }
