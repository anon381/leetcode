class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ n * (1 - n) // 2] + list(range(1, n))


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
